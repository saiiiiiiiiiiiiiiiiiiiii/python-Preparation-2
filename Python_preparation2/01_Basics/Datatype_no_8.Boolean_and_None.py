# The Boolean type in Python is a built-in data type that represents truth values: True and False. 
# Booleans are a fundamental part of programming and are often used in conditional statements, loops, and logical operations.
# Boolean Values
# In Python, the Boolean type has two possible values:

# True: Represents the truth value true.
# False: Represents the truth value false.

# These values are actually instances of the bool class, which is a subclass of the int class.


# Creating Booleans
# Boolean values are typically created as the result of comparisons or logical operations:
# Boolean values
a = True
b = False

# Boolean from comparison
x = 10
y = 20
is_equal = (x == y)  # Output: False
is_not_equal = (x != y) #  Output: True
print(is_not_equal)


# Boolean Operations
# Booleans are used in logical operations that return either True or False:



# Logical AND (and)
# Returns True if both operands are True; otherwise, it returns False.
result = (5 > 3) and (8 < 10)  # Output: True
print(result)


# Logical OR (or)
# Returns True if at least one of the operands is True; otherwise, it returns False.
result = (5 > 3) or (8 > 10)  # Output: True
print(result)


# Logical NOT (not)
# Returns True if the operand is False; otherwise, it returns False.
result = not (5 > 3)  # Output: False
print(result)




# Truthiness
# In Python, other values can be evaluated in a Boolean context to determine their "truthiness" or "falsiness." This is useful for conditions and loops.
# Truthy Values
# Most values are considered "truthy," meaning they evaluate to True in a Boolean context. For example:
if "hello":
    print("This is truthy")  # Output: This is truthy


# Falsy Values
# Certain values are considered "falsy," meaning they evaluate to False in a Boolean context:

# None
# False
# Numeric zero values: 0, 0.0
# Empty sequences and collections: '', (), [], {}, set()

if not []:
    print("This is falsy")  # Output: This is falsy


# Boolean Type Conversion
# You can explicitly convert other data types to Boolean using the bool() function:

# Convert various types to Boolean
print(bool(1))          # Output: True
print(bool(0))          # Output: False
print(bool('text'))     # Output: True
print(bool(''))         # Output: False
print(bool([]))         # Output: False
print(bool([1, 2, 3]))  # Output: True


# Boolean in Conditional Statements
# Booleans are commonly used in if, elif, and else statements:


# None Type 
# In Python, None is a special constant that represents the absence of a value or a null value.
# It is a fundamental part of Python and is used in various scenarios to signify that something is not set, not available, or empty.


# Characteristics of None
# Singleton: There is exactly one instance of None in a Python runtime. It is a singleton, meaning that all occurrences of None are the same object.
# Data Type: None is of the type NoneType, which is a unique type in Python.
print(type(None)) # Output: <class 'NoneType'>



# Falsy Value: In a Boolean context, None is considered False. It is treated as falsy in conditional statements and logical expressions.

if not None:
    print("None is falsy")  # Output: None is falsy



# Common Uses of None
# Default Function Arguments: It is commonly used as a default value for function arguments to indicate that no argument was passed or that the argument is optional.
def greet(name = None):
    if name is None:
        print("Hello, World!")
    else:
        print(f"Hello, {name}!")
      
greet()

# Placeholder for Optional Values: It can be used to represent an optional value that might be set later.
result = None
# Some code that might update result
if result is None:
    print("Result is not yet set.")


# Return Value for Functions: 
# Functions that do not explicitly return a value will return None by default. 
# This is useful for functions that perform actions but do not need to return a result.

def print_message(message):
    print(message)

return_value = print_message("Hello!")  # Output: Hello!
print(return_value)  # Output: None


# Representing Empty Data Structures: 
# None can be used to represent the absence of data in data structures or class attributes.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node = Node(10)
print(node.next)  # Output: None


# Comparison with Other Values
# Comparison with None: Use is to check for None instead of ==, which compares values rather than identities.
a = None
b = None
print(a is b)  # Output: True



# Comparison with Other Falsy Values: While None is falsy, it is distinct from other falsy values like 0, '' (empty string), [] (empty list), and {} (empty dictionary).
if None == 0:
    print("None equals 0")  # This will not print



