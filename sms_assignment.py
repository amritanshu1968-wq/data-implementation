
class Student:

    # Constructor to initialize student details
    def __init__(self, roll, name, age, course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course

    # Converts object into string format for storing in file
    def __str__(self):
        return f"{self.roll},{self.name},{self.age},{self.course}"


# Name of the text file where student records are stored
FILE_NAME = "students.txt"


# Function : Add Student

def add_student():

    print("\n----- Add Student -----")

    # Taking input from the user
    roll = input("Enter Roll Number : ")
    name = input("Enter Name        : ")
    age = input("Enter Age         : ")
    course = input("Enter Course      : ")

    # Creating Student object
    student = Student(roll, name, age, course)

    # Writing student details into file
    with open(FILE_NAME, "a") as file:
        file.write(str(student) + "\n")

    print("\nStudent Added Successfully!")



# Function : View Students

def view_students():

    print("\n----- Student Records -----")

    try:

        # Open file in read mode
        with open(FILE_NAME, "r") as file:

            records = file.readlines()

            # Check if file is empty
            if len(records) == 0:
                print("No Student Records Found.")
                return

            # Display every student record
            for line in records:

                roll, name, age, course = line.strip().split(",")

                print("--------------------------------")
                print("Roll Number :", roll)
                print("Name        :", name)
                print("Age         :", age)
                print("Course      :", course)

            print("--------------------------------")

    # Handle file not found error
    except FileNotFoundError:
        print("students.txt file does not exist.")


# Function : Search Student

def search_student():

    roll = input("\nEnter Roll Number to Search : ")

    try:

        with open(FILE_NAME, "r") as file:

            found = False

            # Search every record
            for line in file:

                r, name, age, course = line.strip().split(",")

                if r == roll:
                    print("\nStudent Found")
                    print("-------------------------")
                    print("Roll Number :", r)
                    print("Name        :", name)
                    print("Age         :", age)
                    print("Course      :", course)

                    found = True
                    break

            # If roll number is not found
            if not found:
                print("Student Not Found.")

    except FileNotFoundError:
        print("students.txt file does not exist.")


# Function : Update Student
def update_student():

    roll = input("\nEnter Roll Number to Update : ")

    try:

        # Read all records
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        updated = False

        # Rewrite the file
        with open(FILE_NAME, "w") as file:

            for line in students:

                r, name, age, course = line.strip().split(",")

                # If roll number matches, update details
                if r == roll:

                    print("\nEnter New Details")

                    name = input("Enter Name   : ")
                    age = input("Enter Age    : ")
                    course = input("Enter Course : ")

                    file.write(f"{r},{name},{age},{course}\n")

                    updated = True

                else:
                    file.write(line)

        if updated:
            print("Student Updated Successfully!")
        else:
            print("Student Not Found.")

    except FileNotFoundError:
        print("students.txt file does not exist.")



# Function : Delete Student

def delete_student():

    roll = input("\nEnter Roll Number to Delete : ")

    try:

        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        deleted = False

        # Rewrite file without deleted student
        with open(FILE_NAME, "w") as file:

            for line in students:

                r, name, age, course = line.strip().split(",")

                if r != roll:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found.")

    except FileNotFoundError:
        print("students.txt file does not exist.")


# Main Program


while True:

    print("\n===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    # Taking user's choice
    choice = input("\nEnter Your Choice : ")

    # Execute corresponding function
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
        print("\nThank You for Using Student Management System!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")