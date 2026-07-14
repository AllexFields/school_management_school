class Student:

    def __init__(self, std_id, std_name, age, standard, guard_c_no):
        self.std_id = std_id
        self.std_name = std_name
        self.age = age
        self.standard = standard
        self.guard_c_no = guard_c_no

    def display(self):
        print("\nStudent Details")
        print("----------------------------")
        print(f"Student ID : {self.std_id}")
        print(f"Name       : {self.std_name}")
        print(f"Age        : {self.age}")
        print(f"Standard   : {self.standard}")
        print(f"Contact No : {self.guard_c_no}")
