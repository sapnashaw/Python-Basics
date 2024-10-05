#  Explain the concept of type casting in Python with examples.


#Sure! Here’s a brief overview of type casting in Python:

#Type Casting** is the process of converting a variable from one data type to another. Here are some common conversions:

#1. **Integer to Float:**
   
x = 5
y = float(x)  # y = 5.0
   

#2. **Float to Integer:**
   
x = 5.67
y = int(x)    # y = 5 (truncates decimal)
   

#3. **String to Integer/Float:**
   
s = "123"
num = int(s)  # num = 123

s = "12.34"
num = float(s)  # num = 12.34
   

#4. **Integer/Float to String:**
   
x = 42
s = str(x)  # s = "42"
   

#5. **List to Tuple and Tuple to List:**

my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # my_tuple = (1, 2, 3)

my_tuple = (4, 5, 6)
my_list = list(my_tuple)  # my_list = [4, 5, 6]
   

#6. **To Boolean:**

print(bool(0))      # Output: False
print(bool(123))    # Output: True


### Use Case:
#Type casting is essential when you need to perform arithmetic operations on user input, which is usually in string format:

age = int(input("Enter your age: "))  # Converts input string to integer


#Type casting helps ensure data compatibility for various operations in Python!