#wap using oop concept Library management system including: add student, Issue book, Search Book, Delete Student detail, Payment late, Submit book



class Student:

    # Constructor
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.book = None

    # Display Student Details
    def display(self):
        print("\nStudent ID :", self.student_id)
        print("Student Name :", self.name)
        print("Issued Book :", self.book)


# Library Class
class Library:

    # Constructor
    def __init__(self):
        self.students = {}

    # Add Student
    def add_student(self):
        student_id = input("Enter Student ID : ")
        name = input("Enter Student Name : ")

        self.students[student_id] = Student(student_id, name)

        print("\nStudent Added Successfully!")

    # Issue Book
    def issue_book(self):
        student_id = input("Enter Student ID : ")

        if student_id in self.students:

            book = input("Enter Book Name : ")

            self.students[student_id].book = book

            print("\nBook Issued Successfully!")

        else:
            print("\nStudent Not Found!")

    # Search Book
    def search_book(self):
        book = input("Enter Book Name : ")

        found = False

        for student in self.students.values():

            if student.book == book:

                print("\nBook Found")
                print("Book :", student.book)
                print("Issued To :", student.name)

                found = True

        if not found:
            print("\nBook Not Found!")

    # Delete Student
    def delete_student(self):
        student_id = input("Enter Student ID : ")

        if student_id in self.students:

            del self.students[student_id]

            print("\nStudent Deleted Successfully!")

        else:
            print("\nStudent Not Found!")

    # Submit Book
    def submit_book(self):
        student_id = input("Enter Student ID : ")

        if student_id in self.students:

            if self.students[student_id].book:

                print("\nBook Submitted :", self.students[student_id].book)

                self.students[student_id].book = None

            else:
                print("\nNo Book Issued!")

        else:
            print("\nStudent Not Found!")

    # Payment for Late Submission
    def payment_late(self):
        days = int(input("Enter Late Days : "))

        fine = days * 10

        print("\nLate Fine = ₹", fine)

    # Display All Students
    def display_students(self):

        if len(self.students) == 0:

            print("\nNo Student Record Found!")

        else:

            for student in self.students.values():

                student.display()


# Main Program


library = Library()

while True:

    print("\n========== Library Management System ==========")

    print("1. Add Student")
    print("2. Issue Book")
    print("3. Search Book")
    print("4. Delete Student")
    print("5. Payment for Late Submission")
    print("6. Submit Book")
    print("7. Display Students")
    print("8. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        library.add_student()

    elif choice == "2":
        library.issue_book()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.delete_student()

    elif choice == "5":
        library.payment_late()

    elif choice == "6":
        library.submit_book()

    elif choice == "7":
        library.display_students()

    elif choice == "8":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")