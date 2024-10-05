# How do conditional statements work in Python? Illustrate with examples


#Conditional statements in Python allow you to execute certain blocks of code based on specific conditions. The primary conditional statements are `if`, `elif`, and `else`. Here's how they work:

### Basic Syntax
"""
if condition:
    # Code to execute if condition is true
elif another_condition:
    # Code to execute if the first condition is false and this condition is true
else:
    # Code to execute if all conditions are false
"""



### Examples

#1. **Simple `if` Statement**

age = 18

if age >= 18:
       print("You are an adult.")
   
#   **Output:**  
   
#   You are an adult.
   

#2. **`if` and `else` Statement**
   
age = 16
if age >= 18:
       print("You are an adult.")
else:
       print("You are a minor.")
   
#   **Output:**  
   
#   You are a minor.
   

#3. **Using `elif`**
   
score = 85
if score >= 90:
       print("Grade: A")
elif score >= 80:
       print("Grade: B")
elif score >= 70:
       print("Grade: C")
else:
       print("Grade: D")
   
#   **Output:**  
   
#   Grade: B
   

#4. **Multiple Conditions with Logical Operators**

age = 25
has_license = True

if age >= 18 and has_license:
       print("You can drive.")
else:
       print("You cannot drive.")
   
#   **Output:**  
   
#   You can drive.
   

#5. **Nested Conditional Statements**
   
num = 10
if num > 0:
       print("Positive number")
       if num % 2 == 0:
           print("Even number")
       else:
           print("Odd number")
else:
       print("Negative number")
   
#   **Output:**  
   
 #  Positive number
 #  Even number
   

#6. **Using `pass` in Conditions**
 #  If you want to include a conditional statement but do not want to execute any code, you can use the `pass` statement:

num = 0
if num > 0:
       print("Positive")
elif num < 0:
       print("Negative")
else:
       pass  # No action needed for zero
   
"""
### Summary
- **`if`**: Checks a condition and executes the block if true.
- **`elif`**: Checks another condition if the previous `if` was false.
- **`else`**: Executes if all previous conditions are false.
- Conditions can use logical operators (`and`, `or`, `not`) to combine multiple checks.

Conditional statements allow your program to make decisions and execute different code paths based on varying conditions, making your code dynamic and responsive.

"""