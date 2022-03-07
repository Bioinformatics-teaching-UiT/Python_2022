"""
This script creates the Student class
Student has the following:

Attributes: gender, age, ID
Methods: get_all_info

class NameofClass():
    __init__
    attributes
    methods
"""

class Student:
    def __init__(self, gender, age, ID):
        self.gender = gender
        self.age = age
        self.ID = ID

    def get_all_info(self):
        return [self.gender, self.age, self.ID]

# create an instance of the Student class called anne
anne = Student('female', 23, 1234)
print(anne.get_all_info())

# print out the attributes of anne
print("Anne's gender is: ", anne.gender)
print("Anne's age is: ", anne.age)
print("Anne's student ID is: ", anne.ID)

# create another instance of the Student class
yin = Student('female', 27, 5555)