import re         # Used for validating input using regular expressions

# Class to represent a student
class SchoolManagement:
    def __init__(self,std_id,std_name,age,standard,guard_c_no):
        self.std_id=std_id
        self.std_name=std_name
        self.age=age
        self.standard=standard
        self.guard_c_no=guard_c_no

    # Method to display student details    
    def display(self):
        print(f"ID: {self.std_id}\n\tName: {self.std_name}\n\tAge: {self.age}\n\tStandard: {self.standard}\n\tContact No: {self.guard_c_no}")

# List to store all student objects (acts like a database)        
lst_of_students=[]

# Auto-increment student ID
std_ID=1      

# Main menu-driven loop
while True:
    print("\n1. New Admission\n2. View Student Details\n3. Update Student Info\n4. Remove Student Record\n5. Exit System")
    user_choice=int(input("Choose from the list and Enter a valid number(1-5): "))

    # Validate menu choice
    if user_choice<1 or user_choice>5:
        print(f"\n{user_choice} is an invalid input.\nEnter a number from 1 to 5 only!!")
        continue

    match user_choice:

        # --------------------------- CASE 1: ADD STUDENT -------------------------------------
        case 1:
            print("\nYou've choosen option 1.\nNow you need to enter all fields one by one.")
            
            # Validate student name (only alphabets allowed)
            while True:
                std_name=input("Enter student's name: ").title()
                check_name=std_name.split()

                if all(i.isalpha() for i in check_name):
                    print(f"\'{std_name}\' has been accepted.")
                    break
                else:
                    print(f"\'{std_name}\' is invalid. Only alphabets are allowed.")

            # Validate age (must be between 5 and 18)
            while True: 
                age=input("\nEnter student's age: ") 
                if age.isdigit(): 
                    age=int(age) 
                    if 5<=age<=18: 
                        print(f"Age {age} is accepted") 
                        break 
                    else: print(f"\"{age}\" is invalid.\nAge must be between 5 & 18") 
                else: print(f"Invalid age. \"{age}\" is not a number")

            # Validate standard (1–12)
            while True:
                choice_standard=input("\nEnter standard you want to get enrolled in: ")
                if choice_standard.isdigit():
                    choice_standard=int(choice_standard)
                    if 1<=choice_standard<=12:
                        print(f"You've Choosen {choice_standard}th standard")
                        break
                    else:
                        print(f"\"{choice_standard}\" is invalid. Choose standard between 1-12")
                else:
                    print(f"Invalid Input. Enter numbers")

            # Validate guardian contact number using regex
            pattern=r'^[6-9]\d{9}$'
            while True:
                guard_c_no=input("\nEnter Guardian's or Parents' contact number: ")
                if re.match(pattern,guard_c_no):
                    print(f"{guard_c_no} is valid and has been registered.")
                    break
                else:
                    print(f"{guard_c_no} is invalid\n\"NOTE:-\" Phone number should start 6-9 and only 10 digits")

            # Creating objects to store data of each student and then append it into lst to store them
            student=SchoolManagement(std_ID,std_name,age,choice_standard,guard_c_no)
            lst_of_students.append(student)

            std_ID+=1              # Increment ID for next student

            print("Student registered successfully!")


        # --------------------------- CASE 2: VIEW STUDENTS ----------------------------
        case 2:
            print(f"You've choosen option 2")

            # View student details
            print("\n1. Search by ID\n2. View all students")

            while True:
                choose=int(input('\nEnter your choice: '))
                if choose in (1,2):
                    break
                else:
                    print(f"{choose} is an invalid choice.\nEnter either\"1\" or \"2\"")

            match choose:
                # Search by student ID
                case 1:
                    search_std=int(input("Enter student ID you want to search: "))
                    for i in lst_of_students:
                        if i.std_id==search_std:
                            i.display()

                # Display all students            
                case 2:
                    for i in lst_of_students:
                        i.display()


        # ------------------------- CASE 3: UPDATE STUDENT --------------------------      
        case 3:
            #Update Student's Information
            search_id=int(input("Enter student ID you want to update: "))
            for i in lst_of_students:
                if i.std_id==search_id:
                    # Present Information of the student
                    print("\nRecord of the student is following:-")
                    i.display()

                    upd_choice=int(input("\nChoose either one of the following options:\n1. To Update Standard\n2. To update Guardian's Contact No "))

                    match upd_choice:

                        # Updating Standard of existing student
                        case 1:
                            print(f"\nYou've choosen to update the standard of the student with name: {i.std_name}")
                            while True:
                                upd_value=int(input("\nEnter new Standard of the student: "))
                                if upd_value<1 or upd_value>12:
                                    print(f"\n{upd_value} is invalid standard.\nEnter standard from 1-12 only")
                                    continue
                                old_std=i.standard
                                i.standard=upd_value
                                print(f'Standard has been changed from \'{old_std}\' to \'{i.standard}\'')
                                break

                        # Updating Guardian's Contact No
                        case 2:
                            print(f"\nYou've choosen to update the contact no of Guardian of the student: {i.std_name}")
                            while True:
                                upd_contact=input('\nEnter new contact no of Guardian: ')
                                if re.match(pattern,upd_contact):
                                    print(f"{upd_contact} is valid.\n{guard_c_no} has been changed with {upd_contact}.")
                                    break
                                else:
                                    print(f"{upd_contact} is invalid\n\"NOTE:-\" Phone number should start 6-9 and only 10 digits")
                else:
                    print(f"{search_id} is not found.")


        # -------------------------- CASE 4: DELETE STUDENT -----------------------------
        case 4:
            # Remove record of a student
            while True:
                delete_choice=int(input("\nTo remove record of a student enter his or her unique student id: "))
                if delete_choice<1:
                    print(f"\'{delete_choice}\' is wrong input. Student ID can't be less than 1.\nEnter value higher than 1")
                    continue
                else:
                    for i in lst_of_students:
                        if i.std_id==delete_choice:
                            lst_of_students.remove(i)
                            print("Student removed successfully")
                break


        # ------------------------ CASE 5: EXIT ------------------------
        case 5:
            print("User has exited the system successfully")
            break