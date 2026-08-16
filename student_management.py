students = {}


def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    students[roll_no] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    for roll_no, student in students.items():
        print(f"\nRoll No: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")


def search_student():
    roll_no = input("Enter roll number to search: ")

    if roll_no in students:
        student = students[roll_no]
        print("\nStudent Found!")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")

    if roll_no in students:
        students[roll_no]["name"] = input("Enter new name: ")
        students[roll_no]["course"] = input("Enter new course: ")
        students[roll_no]["marks"] = float(input("Enter new marks: "))
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
