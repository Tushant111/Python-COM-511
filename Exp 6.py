def add_student_record(records, roll_number, name, grade):
    student_record = {'Roll Number': roll_number, 'Name': name, 'Grade': grade}
    records.append(student_record)

def search_student_record(records, roll_number):
    for record in records:
        if record['Roll Number'] == roll_number:
            return record
    return None  # Return None if the student record is not found

# Initialize an empty list to store student records
student_records = []

# Get user input to add student records
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    add_student_record(student_records, roll_number, name, grade)

# Get user input to search for a student record
search_roll_number = int(input("\nEnter Roll Number to search: "))
found_record = search_student_record(student_records, search_roll_number)

# Display the result
if found_record:
    print("\nStudent Record Found:")
    for key, value in found_record.items():
        print(f"{key}: {value}")
else:
    print(f"\nStudent Record with Roll Number {search_roll_number} not found.")
