# Compare and contrast mutable and immutable objects in Python with examples.



#In Python, objects can be classified as **mutable** or **immutable** based on whether their value can be changed after they are created.

### Mutable Objects:
#Definition: These objects can be changed after their creation. You can modify, add, or delete elements without creating a new object.
#Examples: Lists, dictionaries, sets.
  
#Example of a mutable object (list):
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
print(my_list)   # Output: [10, 2, 3]

#Here, the list is modified in place without creating a new object.

# Immutable Objects:
#Definition : These objects **cannot be changed** after they are created. Any attempt to modify the object results in creating a new object.
#Examples   : Strings, tuples, integers, floats.

#Example of an immutable object (string):

my_string = "Hello"
my_string = "World"  # Creating a new string object
print(my_string)     # Output: "World"
"""
In this case, a new string is created instead of modifying the original string.

### Key Differences:
| Feature               | Mutable Objects                  | Immutable Objects               |
|-----------------------|-----------------------------------|---------------------------------|
| **Modifiability**      | Can be modified in place          | Cannot be modified; new object created |
| **Examples**           | Lists, dictionaries, sets         | Strings, tuples, integers, floats |
| **Performance**        | Slower for large modifications    | Faster for read-only operations  |
| **Memory Efficiency**  | Modifications don’t create new objects | Modifications result in new objects |

Practical Implications:
Mutable objects are useful when you need to store or modify large collections of data efficiently.
Immutable objects ensure data integrity, which makes them suitable for use in hashable collections like dictionary keys and set elements.
"""