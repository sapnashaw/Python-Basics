#  Describe the different types of loops in Python and their use cases with examples.



# Different Types of Loops in Python

# 1. For Loop
# The for loop is used to iterate over a sequence (like a list, tuple, string, or range).
# Syntax:
# for variable in sequence:
#     # Code to execute

# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

# Use Case:
# - Iterating over elements in a collection (like lists, tuples, or strings).
# - Useful for performing operations on each element in a collection.


# 2. While Loop
# The while loop continues to execute as long as a specified condition is true.
# Syntax:
# while condition:
#     # Code to execute

# Example:
count = 1
while count <= 5:
    print(count)  # Output: 1, 2, 3, 4, 5
    count += 1  # Increment count to avoid infinite loop

# Use Case:
# - When the number of iterations is not known beforehand and depends on a condition.
# - Commonly used for input validation, processing data until a specific condition is met, etc.


# 3. Loop Control Statements
# Python also provides control statements to modify loop behavior:

# a. Break Statement
# The break statement terminates the loop and transfers control to the statement following the loop.

# Example:
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)  # Output: 0, 1, 2, 3, 4

# b. Continue Statement
# The continue statement skips the current iteration and continues with the next iteration of the loop.

# Example:
for num in range(5):
    if num == 2:
        continue  # Skip the iteration when num is 2
    print(num)  # Output: 0, 1, 3, 4

# c. Else Statement with Loops
# You can use an else statement with both for and while loops.
# The else block executes after the loop completes normally (not via break).

# Example:
for num in range(3):
    print(num)  # Output: 0, 1, 2
else:
    print("Loop completed without break.")  # This runs after the loop

# Summary of Use Cases:
# - For Loops: Best for iterating over collections, such as lists, strings, or any iterable objects where the number of iterations is known.
# - While Loops: Ideal for situations where the number of iterations is unknown and depends on dynamic conditions.
# - Control Statements: Allow fine-tuning of loop execution flow for specific requirements.
