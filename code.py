# ----------------------------------------------------
# STUDENT PERFORMANCE MANAGER PROJECT
# Covers: Functions, Loops, Conditions, OOP, Inheritance,
# Error handling, Lists, Dictionaries, File Handling
# ----------------------------------------------------

students = []  # list to store student dictionaries


# ----------------------- FUNCTIONS -----------------------

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'
    
def add_student(name, marks):
    """Add new student to the list."""
    try:
        marks = float(marks)
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
            

        students.append({"name": name, "marks": marks})
        print(f"{name} added successfully!")

    except ValueError as err:
        print("Error:", err)


def update_marks(name, new_marks):
    """Update marks of an existing student."""
    try:
        new_marks = float(new_marks)
        if new_marks < 0 or new_marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        for student in students:
            if student["name"].lower() == name.lower():
                student["marks"] = new_marks
                print(f"Marks updated for {name}!")
                return
            
        print("Student not found!")

    except ValueError as err:
        print("Error:", err)


def show_all_students():
    """Display all students with grades."""
    if not students:
        print("No students available yet!")
        return

    print("\n------ All Students ------")
    for s in students:
        print(f"Name: {s['name']}, Marks: {s['marks']}, Grade: {calculate_grade(s['marks'])}")


# ----------------------- OOP CLASSES -----------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = float(marks)

    def get_grade(self):
        return calculate_grade(self.marks)

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Grade: {self.get_grade()}")


class ScholarStudent(Student):
    def __init__(self, name, marks, scholarship_amount):
        super().__init__(name, marks)
        self.scholarship_amount = scholarship_amount

    def display_info(self):
        super().display_info()
        print(f"Scholarship Amount: ₹{self.scholarship_amount}")


# ----------------------- FILE HANDLING -----------------------

def generate_report():
    """Create a report file with summary."""
    if not students:
        print("No student data available to generate report.")
        return

    try:
        total = len(students)
        marks_list = [s["marks"] for s in students]
        avg = sum(marks_list) / total
        highest = max(marks_list)
        lowest = min(marks_list)

        grade_count = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0
        }

        for s in students:
            grade_count[calculate_grade(s["marks"])] += 1

        with open("report.txt", "w") as file:
            file.write("---- STUDENT PERFORMANCE REPORT ----\n")
            file.write(f"Total Students: {total}\n")
            file.write(f"Average Marks: {avg:.2f}\n")
            file.write(f"Highest Marks: {highest}\n")
            file.write(f"Lowest Marks: {lowest}\n")
            file.write("\nGrade Count:\n")

            for grade, count in grade_count.items():
                file.write(f"{grade}: {count}\n")

        print("Report generated successfully! (report.txt)")

    except Exception as e:
        print("Error while generating report:", e)


# ----------------------- MENU PROGRAM -----------------------

while True:
    print("\n===== STUDENT PERFORMANCE MANAGER =====")
    print("A. Add Student")
    print("B. Update Marks")
    print("C. Show All Students")
    print("D. Generate Report")
    print("E. Create Scholar Student (OOP Demo)")
    print("F. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        add_student(name, marks)

    elif choice == 'B':
        name = input("Enter name of student: ")
        marks = input("Enter new marks: ")
        update_marks(name, marks)

    elif choice == 'C':
        show_all_students()

    elif choice == 'D':
        generate_report()

    elif choice == 'E':
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        scholarship = input("Enter scholarship amount: ")

        try:
            scholar = ScholarStudent(name, float(marks), scholarship)
            scholar.display_info()
        except ValueError:
            print("Invalid marks!")

    elif choice == 'F':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")