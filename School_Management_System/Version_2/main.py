import re

from operations import (
    add_student,
    view_all_students,
    search_student,
    update_standard,
    update_contact,
    delete_student
)


def get_name():

    while True:

        name = input("\nEnter Student Name : ").title().strip()

        words = name.split()

        if name and all(word.isalpha() for word in words):

            return name

        print("Invalid Name. Only alphabets are allowed.")



def get_age():

    while True:

        age = input("Enter Age : ")

        if age.isdigit():

            age = int(age)

            if 5 <= age <= 18:

                return age

        print("Age should be an integer and it should be between 5 and 18.")



def get_standard():

    while True:

        standard = input("Enter Standard (1-12): ")

        if standard.isdigit():

            standard = int(standard)

            if 1 <= standard <= 12:

                return standard

        print("Invalid Standard.")



def get_contact():

    pattern = r"^[6-9]\d{9}$"

    while True:

        contact = input("Enter Guardian Contact Number : ")

        if re.match(pattern, contact):

            return contact

        print("Invalid Contact Number.")

# -------------- Main-Menu ----------------

while True:

    print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")

    print("1. New Admission")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter Choice : ")

    if not choice.isdigit():

        print("Invalid Input.")
        continue

    choice = int(choice)

# ------------- New Admission ---------------

    if choice == 1:

        print("\nNEW ADMISSION")

        name = get_name()

        age = get_age()

        standard = get_standard()

        contact = get_contact()

        add_student(
            name,
            age,
            standard,
            contact
        )

# ------------- Search Or View Students ---------------

    elif choice == 2:

        print("\n1. Search Student")

        print("2. View All Students")

        sub = input("Choose : ")

        if sub == "1":

            student_id = int(input("Enter Student ID : "))

            search_student(student_id)

        elif sub == "2":

            view_all_students()

        else:

            print("Invalid Choice")

# ------------- Update Standard Or Contact ---------------

    elif choice == 3:

        student_id = int(input("Enter Student ID : "))

        print("\n1. Update Standard")

        print("2. Update Contact")

        option = input("Choose : ")

        if option == "1":

            new_standard = get_standard()

            update_standard(
                student_id,
                new_standard
            )

        elif option == "2":

            new_contact = get_contact()

            update_contact(
                student_id,
                new_contact
            )

        else:

            print("Invalid Choice")

# ------------- Delete Record ---------------

    elif choice == 4:

        student_id = int(input("Enter Student ID : "))

        delete_student(student_id)

# ------------- Exit Program ---------------

    elif choice == 5:

        print("\nThank You!")

        break

    else:

        print("Enter number between 1 and 5.")