from datetime import datetime, timedelta
# Student Class
class Student:

    # Constructor
    def __init__(self, student_id, name, mobile):
        self.student_id = student_id
        self.name = name
        self.mobile = mobile
        self.book_id = None
        self.book = None

    # Display Student Details
def display(self):

    print("\n========== Student Details")

    print("Student ID   :", self.student_id)
    print("Student Name :", self.name)
    print("Mobile No.   :", self.mobile)
    print("Book ID      :", self.book_id)
    print("Issued Book  :", self.book)
    print("Issue Date   :", self.issue_date)
    print("Due Date     :", self.due_date)


# Library Class
class Library:

    # Constructor
   
  def __init__(self, student_id, name, mobile):
    self.student_id = student_id
    self.name = name
    self.mobile = mobile
    self.book_id = None
    self.book = None

    # New Attributes
    self.issue_date = None
    self.due_date = None

        # Predefined Books
    self.books = {
            "B101": "Python Programming",
            "B102": "Data Structures",
            "B103": "DBMS",
            "B104": "Operating System",
            "B105": "Computer Networks"
        }

    # Add Student
    def add_student(self):

        student_id = input("Enter Student ID : ")
        name = input("Enter Student Name : ")
        mobile = input("Enter Mobile Number : ")

        self.students[student_id] = Student(student_id, name, mobile)

        print("\nStudent Added Successfully!")

    # Issue Book
    def issue_book(self):

        student_id = input("Enter Student ID : ")

        if student_id in self.students:

            print("\nAvailable Books")

            for id, book in self.books.items():
                print(id, ":", book)

            book_id = input("\nEnter Book ID : ")

            if book_id in self.books:

                self.students[student_id].book_id = book_id
                self.students[student_id].book = self.books[book_id]

                print("\nBook Issued Successfully!")

            else:
                print("\nInvalid Book ID!")

        else:
            print("\nStudent Not Found!")

    # Search Book
    def search_book(self):

        book = input("Enter Book Name : ")

        found = False

        for student in self.students.values():

            if student.book == book:

                print("\nBook Found")
                print("Book ID   :", student.book_id)
                print("Book Name :", student.book)
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
                self.students[student_id].book_id = None

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


# ===========================
# Main Program
# ===========================

library = Library()

while True:

    print("\n========== SMART LIBRARY MANAGEMENT SYSTEM ==========")

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