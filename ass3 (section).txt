# student_management.py

students = {
    "ST101": {"name": "John Smith", "age": 20, "grades": [85, 90, 88]},
    "ST102": {"name": "Emma Davis", "age": 19, "grades": [55, 60, 58]},
    "ST103": {"name": "Alex Johnson", "age": 21, "grades": [95, 92, 96]},
}

# Task 2: Grade Processing
def process_grades(student_id):
    if student_id not in students:
        return "Student ID not found."

    grades = students[student_id]["grades"]
    avg_grade = sum(grades) / len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)
    status = "Pass" if avg_grade >= 60 else "Fail"

    return f"Average: {avg_grade:.2f}, Highest: {highest_grade}, Lowest: {lowest_grade}, Status: {status}"

# Task 3: Student Report
def generate_report():
    print("\nStudent Report")
    print("-" * 50)
    for student_id, details in students.items():
        grades = details["grades"]
        avg_grade = sum(grades) / len(grades)
        status = "Pass" if avg_grade >= 60 else "Fail"
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Status: {status}")
    print("-" * 50)

# Bonus Task Functions
def add_student(student_id, name, age, grades):
    if student_id in students:
        return "Student ID already exists."
    students[student_id] = {"name": name, "age": age, "grades": grades}
    return "Student added successfully."

def update_grades(student_id, new_grades):
    if student_id not in students:
        return "Student ID not found."
    students[student_id]["grades"] = new_grades
    return "Grades updated successfully."

def remove_student(student_id):
    if student_id not in students:
        return "Student ID not found."
    del students[student_id]
    return "Student removed successfully."

def sort_students_by_average():
    print("\nStudents Sorted by Average Grade:")
    print("-" * 50)
    sorted_students = sorted(
        students.items(),
        key=lambda x: sum(x[1]["grades"]) / len(x[1]["grades"]),
        reverse=True
    )
    for student_id, details in sorted_students:
        avg = sum(details["grades"]) / len(details["grades"])
        print(f"ID: {student_id}, Name: {details['name']}, Avg: {avg:.2f}")
    print("-" * 50)

# CLI Menu
def menu():
    while True:
        print("\n=== Student Management System ===")
        print("1. Process Grades")
        print("2. Generate Report")
        print("3. Add Student")
        print("4. Update Grades")
        print("5. Remove Student")
        print("6. Sort Students by Average")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            print(process_grades(sid))
        elif choice == "2":
            generate_report()
        elif choice == "3":
            sid = input("Enter new Student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grades = list(map(int, input("Enter grades separated by space: ").split()))
            print(add_student(sid, name, age, grades))
        elif choice == "4":
            sid = input("Enter Student ID: ")
            grades = list(map(int, input("Enter new grades separated by space: ").split()))
            print(update_grades(sid, grades))
        elif choice == "5":
            sid = input("Enter Student ID to remove: ")
            print(remove_student(sid))
        elif choice == "6":
            sort_students_by_average()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()