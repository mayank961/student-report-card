import os
import json

class StudentsReportCard:
    def __init__(self):
        self.file_path = "students_card/students.json"
        os.makedirs("students_card", exist_ok=True)

        try:
            with open(self.file_path, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = []

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.students, file, indent=2)

    def add_new_student(self, name, roll_number, marks):
        for student in self.students:
            if student["roll_number"] == roll_number:
                print("⚠️ This Roll Number already exists.")
                return
        new_student = {"name": name, "roll_number": roll_number, "marks": marks}
        self.students.append(new_student)
        self.save_data()
        print("✅ Student added successfully.")

    def search_student(self, roll_number):
        for student in self.students:
            if student["roll_number"] == roll_number:
                print(f"🎯 Student Found!\nName: {student['name']}\nRoll No: {student['roll_number']}\nMarks: {student['marks']}")
                return
        print("❌ Student not found.")

    def display_all_student(self):
        if not self.students:
            print("⚠️ No students found.")
            return
        print("\n📜 All Students Report Card:")
        print("-" * 40)
        for student in self.students:
            print(f"Name: {student['name']}, Roll No: {student['roll_number']}, Marks: {student['marks']}")
        print("-" * 40)

    def update_marks(self, roll_number, new_marks):
        for student in self.students:
            if student["roll_number"] == roll_number:
                student["marks"] = new_marks
                self.save_data()
                print(f"✅ Marks updated for Roll No {roll_number}.")
                return
        print("❌ Student not found.")

    def delete_student(self, roll_number):
        for student in self.students:
            if student["roll_number"] == roll_number:
                self.students.remove(student)
                self.save_data()
                print(f"❌ Student removed (Roll Number: {roll_number})")
                return
        print("❌ Student not found.")


if __name__ == "__main__":
    report = StudentsReportCard()

    while True:
        print("\n=============")
        print("1. Add New Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        print("==============")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            try:
                name = input("Enter Name: ")
                roll_number = int(input("Enter Roll Number: "))
                marks = {"Math": int(input("Enter Math Marks: ")),
                        "Science": int(input("Enter Science Marks: ")),
                        "English": int(input("Enter English Marks: "))}
                report.add_new_student(name, roll_number, marks)
            except ValueError:
                print("❌ Invalid input. Please enter correct values.")

        elif user_input == "2":
            try:
                roll_number = int(input("Enter Roll Number: "))
                report.search_student(roll_number)
            except ValueError:
                print("❌ Invalid Roll Number.")

        elif user_input == "3":
            report.display_all_student()

        elif user_input == "4":
            try:
                roll_number = int(input("Enter Roll Number: "))
                updated_marks = int(input("Enter Updated Marks: "))
                report.update_marks(roll_number, updated_marks)
            except ValueError:
                print("❌ Invalid input.")

        elif user_input == "5":
            try:
                roll_number = int(input("Enter Roll Number to delete: "))
                report.delete_student(roll_number)
            except ValueError:
                print("❌ Invalid Roll Number.")

        elif user_input == "6":
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1-6.")
