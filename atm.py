class Bank:
    def __init__(self):
        self.users = {}  # Placeholder for user data
        self.admin_username = "tushant"
        self.admin_password = "password"

    def create_user(self, username, password, balance=0):
        if username not in self.users:
            self.users[username] = {"password": password, "balance": balance}
            print(f"User {username} created successfully.")
        else:
            print(f"User {username} already exists.")

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False

    def get_balance(self, username):
        return self.users[username]["balance"]

    def deposit(self, username, amount):
        self.users[username]["balance"] += amount
        print(f"Deposit successful. New balance: ${self.get_balance(username)}")

    def withdraw(self, username, amount):
        if amount <= self.get_balance(username):
            self.users[username]["balance"] -= amount
            print(f"Withdrawal successful. New balance: ${self.get_balance(username)}")
        else:
            print("Insufficient funds.")

# ATM Application
def main():
    bank = Bank()

    while True:
        print("\nWelcome to the ATM Application")
        print("1. Login as User")
        print("2. Login as Admin")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if bank.authenticate_user(username, password):
                while True:
                    print("\nUser Menu:")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        print(f"Your balance: ${bank.get_balance(username)}")
                    elif user_choice == "2":
                        amount = float(input("Enter deposit amount: $"))
                        bank.deposit(username, amount)
                    elif user_choice == "3":
                        amount = float(input("Enter withdrawal amount: $"))
                        bank.withdraw(username, amount)
                    elif user_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Try again.")

            else:
                print("Authentication failed. Invalid username or password.")

        elif choice == "2":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")

            if admin_username == bank.admin_username and admin_password == bank.admin_password:
                print("\nAdmin Menu:")
                print("1. Create User")
                print("2. Exit")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    new_username = input("Enter new username: ")
                    new_password = input("Enter new password: ")
                    bank.create_user(new_username, new_password)
                elif admin_choice == "2":
                    print("Logged out.")
                else:
                    print("Invalid choice.")

            else:
                print("Admin authentication failed. Invalid username or password.")

        elif choice == "3":
            print("Exiting ATM Application. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
