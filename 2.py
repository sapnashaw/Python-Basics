#  Describe the role of predefined keywords in Python and provide examples of how they are used in a
#  program.


"""
Predefined keywords in Python are reserved words that have special meanings and cannot be used for variable names or identifiers. They form the building blocks of Python's syntax and define the structure and flow of a program.
Role of predefined keywords:

    Control the flow of the program, such as loops and conditional statements.
    Define functions and classes for modular and object-oriented programming.
    Handle exceptions and manage errors.
    Work with data types and logical operators.
"""

#Examples of commonly used predefined keywords:

#if, else, elif: Used for conditional statements.
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")


#for, while: Used for loops.
for i in range(3):
    print(i)


#def: Used to define a function:
def greet():
    print("Hello, World!")
greet()


#class: Defines a class.
class Dog:
    def __init__(self, name):
        self.name = name
my_dog = Dog("Buddy")
print(my_dog.name)


#try, except: Handles exceptions.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Predefined keywords are crucial for structuring code and managing logic effectively in Python programs.
