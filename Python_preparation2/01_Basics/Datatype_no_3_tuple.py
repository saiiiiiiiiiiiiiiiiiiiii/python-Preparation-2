# Tuples in Python are another type of sequence data structure, 
# similar to lists but with some key differences. 
# Here's a detailed look at tuples:

# Creating Tuples
# Tuples are created using parentheses () with elements separated by commas:


#Creating an empty tuple 
empty_tuple =  ()

# Creating a tuple with  elements  
fruits = ('Apple', 'Bananna', 'Cherry')

# Tuples can contain different type of an elements 
mixed_tuple = (1, 'hello', 3.14, [1,2,3])
# print(mixed_tuple)

# Single-Element Tuples
# To create a tuple with a single element, include a trailing comma:
single_element_tuple = (1,)
print(single_element_tuple)
print(type(single_element_tuple))
# Without the comma, Python interprets it as a simple parenthesis expression, not a tuple.

# Accessing Elements
# Tuples are indexed just like lists:
fruits = ('Apple', 'Bananna', 'cherry')

# Accessing Elements
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[-1])

# Slicing Tuples
# You can get subsets of tuples using slicing:
print(fruits[0:2]) # output : ('Apple', 'Bananna')

# Tuple Operations
# Concatenation
# You can concatenate tuples using the + operator:

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)


# epetition
# You can repeat tuples using the * operator:

tuple1 = (1, 2, 3)
# print(tuple1 * 5)


# Tuple Methods
# Tuples have fewer methods compared to lists because they are immutable. The primary methods are:

# count()
# Counts the occurrences of a specified element:

numbers = (1,2,1,3,4,3,5,6,4,8,6,7,55,6,44,322,667,55,)
# print(numbers.count(1))

# index()
# Finds the index of the first occurrence of a specified element:
fruits = ('Apple', 'Bananna', 'cherry')
# print(fruits.index('Apple'))
# print(fruits.index('Bananna'))
# print(fruits.index('cherry'))

# Immutability
# The key characteristic of tuples is immutability. Once created, 
# you cannot modify, add, or remove elements:

tuple1 = (1, 2, 3)
# tuple1[0] = 10  # This will raise a TypeError
# print(tuple1)  # Output: (1, 2, 3)  

# However, if a tuple contains mutable objects (like lists), those objects can be modified:
nested_tuple = (1, [2, 3])
nested_tuple[1][0] = 3
# print(nested_tuple)

# Tuple Packing and Unpacking
# Packing
# Creating a tuple with multiple values is called packing:
coordinates = (10, 20)  # Packing two values into a tuple
# print(coordinates)

# Unpacking
# You can extract values from a tuple into individual variables:

x, y = coordinates  # Unpacking the tuple into x and y
print(x, y)

# Example 
coordinates = (10,20,30)
x, y, z = coordinates
print(x)  # Output 10
print(y)  # Output 20
print(z)  # Output 30


# Unpacking with a Single Variable:

# If you have a tuple with a single value, you can still unpack it, but you need to include a comma:

single_value = (2,)
value = single_value
# print(value)

# Nested Tuples
# Tuples can contain other tuples, allowing for multi-level nesting:

nested_tuple = (1, (2, 3), (4, (5, 6)))
element = nested_tuple[1][1]  # Output: 3
print(element)