class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, salary, benefits):
        super().__init__(emp_id, name, salary)
        self.benefits = benefits

    def display_details(self):
        super().display_details()
        print(f"Benefits: {self.benefits}")
        print("Employment Type: Full Time")


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: {self.hourly_rate}")
        print(f"Hours Worked: {self.hours_worked}")
        print("Employment Type: Part Time")


# Get user input for Full Time Employee
full_time_emp_id = int(input("Enter Full Time Employee ID: "))
full_time_name = input("Enter Full Time Employee Name: ")
full_time_salary = float(input("Enter Full Time Employee Salary: "))
full_time_benefits = input("Enter Full Time Employee Benefits: ")

full_time_employee = FullTimeEmployee(full_time_emp_id, full_time_name, full_time_salary, full_time_benefits)

# Get user input for Part Time Employee
part_time_emp_id = int(input("\nEnter Part Time Employee ID: "))
part_time_name = input("Enter Part Time Employee Name: ")
part_time_hourly_rate = float(input("Enter Part Time Employee Hourly Rate: "))
part_time_hours_worked = float(input("Enter Part Time Employee Hours Worked: "))

part_time_employee = PartTimeEmployee(part_time_emp_id, part_time_name, part_time_hourly_rate, part_time_hours_worked)

# Display the details of both employees
print("\nFull Time Employee Details:")
full_time_employee.display_details()

print("\nPart Time Employee Details:")
part_time_employee.display_details()
