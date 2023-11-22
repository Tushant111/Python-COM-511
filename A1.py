import time
import datetime
import json


class User:
    MIN_BALANCE = 5000

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.balance = self.MIN_BALANCE
        self.login_attempts = 0
        self.is_locked = False
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 100000:
            self.balance += amount
            self._update_transaction_history(f"Deposited ${amount} on {self._current_time()}")
            return True
        else:
            print("Maximum deposit limit has been exceeded.")
            return False

    def withdraw(self, amount):
        if amount <= 50000 and self.balance - amount >= self.MIN_BALANCE:
            self.balance -= amount
            self._update_transaction_history(f"Withdrew ${amount} on {self._current_time()}")
            return True
        else:
            print("The withdrawal amount is invalid or insufficient funds have been found.")
            return False

    def check_balance(self):
        return self.balance

    def change_credentials(self, current_password, new_password):
        if self.password == current_password:
            self.password = new_password
            return True
        else:
            print("Current password is invalid. Unable to change credentials.")
            return False

    def add_tag_to_last_transaction(self, tag):
        if self.transaction_history:
            last_transaction = self.transaction_history[-1]
            last_transaction_with_tag = f"{last_transaction} [Tag: {tag}]"
            self.transaction_history[-1] = last_transaction_with_tag
        else:
            print("No transactions available to add a tag.")

    def _current_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")

    def _update_transaction_history(self, transaction):
        self.transaction_history.append(transaction)


class Admin(User):
    MAX_BALANCE = 300000
    MAX_DEPOSIT = 300000

    def __init__(self, user_id, password, atm):
        super().__init__(user_id, password)
        self.atm = atm

    def cash_deposit(self, amount):
        if amount <= self.MAX_DEPOSIT:
            self.balance += amount
            self._update_transaction_history(f"Admin has deposited ${amount} on {self._current_time()}")

            # Update the total balance in the ATM
            self.atm.update_total_balance()

            print(f"Admin Deposit successful! Amount: ${amount}")
            return True
        else:
            print("Maximum deposit limit for admin has been exceeded.")
            return False

    def notify_low_balance(self):
        if self.balance < 75000:
            print("Notification: Admin balance is less than 75k.")


class ATM:
    TIMEOUT_LIMIT = 30

    def __init__(self):
        self.users = {}
        self.admin = Admin("admin", "admin", self)  # Pass the ATM instance to Admin
        self.load_data()

    def load_data(self):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
                for user_id, user_data in data.items():
                    if user_id == "admin":
                        self.admin.balance = user_data.get("balance", 0)
                        self.admin.transaction_history = user_data.get("transaction_history", [])
                    else:
                        user = User(user_id, user_data.get("password", ""))
                        user.balance = user_data.get("balance", 0)
                        user.login_attempts = user_data.get("login_attempts", 0)
                        user.is_locked = user_data.get("is_locked", False)
                        user.transaction_history = user_data.get("transaction_history", [])
                        self.users[user_id] = user
        except FileNotFoundError:
            pass

    def save_data(self):
        data = {"admin": {
            "password": self.admin.password,
            "balance": self.admin.balance,
            "transaction_history": self.admin.transaction_history
        }}
        for user_id, user in self.users.items():
            data[user_id] = {
                "password": user.password,
                "balance": user.balance,
                "login_attempts": user.login_attempts,
                "is_locked": user.is_locked,
                "transaction_history": user.transaction_history
            }
        with open("users.json", "w") as file:
            json.dump(data, file)

    def update_total_balance(self):
        total_balance = sum(user.balance for user in self.users.values())
        self.admin.balance = total_balance

        # Save the updated data
        self.save_data()

        # Update the balance for each user
        for user in self.users.values():
            user.balance = user.balance  # Trigger the setter to update individual user balances

    def create_account(self, user_id, password):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, password)
            self.save_data()
            print("CONGRATULATIONS: Account is successfully created!")
        else:
            print("User ID already exists. Please choose a different one.")

    def change_credentials(self, user_id, current_password, new_password):
        user = self.users.get(user_id)
        if user:
            if user.change_credentials(current_password, new_password):
                self.save_data()
                print(f"Credentials changed successfully for user {user_id}!")
        else:
            print("User not found. Unable to change credentials.")

    def check_timeout(self, last_interaction_time):
        elapsed_time = time.time() - last_interaction_time
        if elapsed_time >= self.TIMEOUT_LIMIT:
            print("\n<<Time limit exceeded. Logout due to inactivity.>>")
            return True
        return False

    def login(self, user_id, password):
        user = self.users.get(user_id)
        if user and not user.is_locked:
            if user.password == password:
                user.login_attempts = 0
                return user
            else:
                user.login_attempts += 1
                if user.login_attempts >= 3:
                    user.is_locked = True
                    print("Account locked due to multiple login failures.")
                else:
                    print("Invalid Password. Attempts remaining:", 3 - user.login_attempts)
        elif user and user.is_locked:
            print("Account is locked. Please contact customer support.")
        else:
            print("\n<<Invalid User ID. Please try again.>>")
        return None

    def display_transaction_history(self, user):
        print("\nTransaction History:")
        for transaction in user.transaction_history:
            print(transaction)

    def admin_menu(self):
        last_interaction_time = time.time()

        while True:
            print("\n------Admin Menu------")
            print("\n(1) Total Balance\n(2) Total Deposit\n(3) Admin Deposit\n(4) Notify Low Balance\n(5) Logout")
            admin_choice = input("\n=> Enter your choice: ")

            if admin_choice == "1":
                total_balance = sum(user.balance for user in self.users.values())
                print("Total Balance: $", total_balance)
            elif admin_choice == "2":
                total_deposit = sum([sum([transaction["amount"] for transaction in user.transaction_history]) for user in self.users.values()])
                print("Total Deposit: $", total_deposit)
            elif admin_choice == "3":
                amount = int(input("Enter deposit amount for admin: $"))
                if self.admin.cash_deposit(amount):
                    print("Admin Deposit successful!")
            elif admin_choice == "4":
                self.admin.notify_low_balance()
            elif admin_choice == "5":
                print("\n<<Admin Logout successful!>>")
                break
            else:
                print("\n<<Invalid choice. Please try again.>>")

            if self.check_timeout(last_interaction_time):
                break

    def user_menu(self, user):
        last_interaction_time = time.time()

        while True:
            print("\n(1) Check Balance\n(2) Deposit\n(3) Withdraw\n(4) Change Password\n(5) Transaction History\n(6) Add Tag to Last Transaction\n(7) Logout")
            user_choice = input("\n=> Enter your choice: ")

            if user_choice:
                last_interaction_time = time.time()

                if user_choice == "1":
                    print("Your balance: $", user.check_balance())
                elif user_choice == "2":
                    amount = int(input("Enter deposit amount: $"))
                    if user.deposit(amount):
                        print("Deposit successful!")
                elif user_choice == "3":
                    amount = int(input("Enter withdrawal amount: $"))
                    if user.withdraw(amount):
                        print("Withdrawal successful!")
                    else:
                        print("\n<<Transaction failed!>>")
                elif user_choice == "4":
                    current_password = input("Enter current password: ")
                    new_password = input("Enter new password: ")
                    self.change_credentials(user.user_id, current_password, new_password)
                elif user_choice == "5":
                    self.display_transaction_history(user)
                elif user_choice == "6":
                    tag = input("Enter tag for the last transaction: ")
                    user.add_tag_to_last_transaction(tag)
                    print("Tag added to the last transaction.")
                elif user_choice == "7":
                    print("\n<<Logout successful!>>")
                    break
                else:
                    print("\n<<Invalid choice. Please try again.>>")

                if self.check_timeout(last_interaction_time):
                    break

    def main(self):
        while True:
            print("\t\t", "-" * 80)
            print("\t\t|", "\t\t\t*** HELLO, WELCOME TO SMART ATM SYSTEM ***", "\t\t|")
            print("\t\t", "-" * 80)
            print("\n------Bank Menu------")
            print("\n(1) Create Account\n(2) Login\n(3) Admin Login\n(4) Exit")
            choice = input("\n=> Enter your choice: ")

            last_interaction_time = time.time()

            if choice == "1":
                user_id = input("\nEnter User ID: ")
                password = input("Enter Password: ")
                self.create_account(user_id, password)
            elif choice == "2":
                user_id = input("Enter User ID: ")
                password = input("Enter Password: ")
                user = self.login(user_id, password)

                if user:
                    print("Login successful!")
                    while True:
                        self.user_menu(user)
                        if self.check_timeout(last_interaction_time):
                            break
            elif choice == "3":
                admin_id = input("Enter Admin ID: ")
                admin_password = input("Enter Admin Password: ")
                admin = self.login(admin_id, admin_password)
                if admin:
                    print("Admin Login successful!")
                    while True:
                        self.admin_menu()
                        if self.check_timeout(last_interaction_time):
                            break
            elif choice == "4":
                print("\nThank you for using the ATM. Goodbye!")
                self.save_data()
                break
            else:
                print("\n<<Invalid choice. Please try again.>>")

            if self.check_timeout(last_interaction_time):
                break

            # Check for timeout every iteration
            if self.check_timeout(last_interaction_time):
                break


if __name__ == "__main__":
    atm = ATM()
    atm.main()
