# Sets in Python are a built-in data type used to store unordered collections of unique items. 
# They are useful for operations that involve membership testing, removing duplicates, and mathematical set operations like union and intersection. 
# Here’s a detailed explanation of sets in Python:


# Creating Sets 
# Sets are created using curly braces {} or the set() constructor:

# Creating an Empty set 
Empty_set = ()

# Creating a set with an elements
fruits = {'Apple', 'Bananna', 'Cherry'}
# print(type(fruits))
# print(fruits)

# Creating a set with a set operator 
numbers = set([1,2,3,4,5])
# print(type(numbers))

# Characteristics
# Unordered: Sets do not maintain any order among their elements. 
# The elements are stored in no particular order.

# Unique Elements: Sets automatically eliminate duplicate elements. 
# If you try to add a duplicate element, it will be ignored.

# Mutable: Sets can be modified after creation. You can add or remove elements,\
# but the elements themselves must be immutable types (e.g., numbers, strings, tuples).

# Basic Set Operations
#        Adding and Removing Elements

# Adding Elements: Use the add() method to add a single element.
fruits = {'Apple', 'Bananna', 'Cherry'}
# print(fruits.add('Pineapple'))
# fruits.add('Pineapple')
# print(fruits)

# Removing Elements: Use remove() to remove an element. 
fruits.remove('Bananna')
# print(fruits)


# Removing and Returning an Arbitrary Element: 
# Use pop() to remove and return an arbitrary element. 
fruits.pop()
# print(fruits)

# Clearing All Elements: Use clear() to remove all elements from the set.

fruits.clear()
# print(fruits)


# Set Operations
# Sets support various mathematical operations that are useful for comparing and combining sets:

# Union
# Combines elements from two sets, removing duplicates:
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9,10}
# print(set1.union(set2))# Output : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# or
# print(set1 | set2)  #  Output : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# Intersection
# Finds elements that are present in both sets:

# print(set1.intersection(set2)) # Output : {5}
# or
# print(set1 & set2) # Implementing intersection by using '&' Operator
# Output : {5}

# Difference
# Finds elements that are in the first set but not in the second:
print(set1.difference(set2)) # Output : {1, 2, 3, 4}
# or
print(set1 - set2)           # Output : {1, 2, 3, 4}


# Symmetric Difference
# Finds elements that are in either of the sets, but not in both:
print(set1.symmetric_difference(set2)) # Output : {1, 2, 3, 4, 6, 7, 8, 9, 10}
# or
print(set1 ^ set2) # Output : {1, 2, 3, 4, 6, 7, 8, 9, 10}


# Set Comprehensions
# You can create sets using comprehensions, similar to list comprehensions:

# Create a set of squares of numbers from 0 to 10:
Squares = {x ** 2 for x in range(11)}
# print(Squares) # Output : {0, 1, 64, 4, 36, 100, 9, 16, 49, 81, 25}

# Set Methods
# copy(): Returns a shallow copy of the set.
Copy_ = Squares.copy()
# print(Copy_)

# issubset(): Checks if the set is a subset of another set.

set = {1,2,3,4,5}
subset = {1,2,3,4,5,6,7,8,9,10}
# print(set.issubset(subset))


# issuperset(): Checks if the set is a superset of another set.
set = {1,2,3,4,5,6,7,8,9, 10}
subset = {1,2,3,4,5}
# print(set.issuperset(subset))
# print(set.issuperset(subset))

# isdisjoint(): Checks if the set has no elements in common with another set.
set = {1,2,3,4,5,6,7,8,9, 10}
subset = {11,12,13,14,15}
# print(set.isdisjoint(subset))



# Set vs. List
# Order: Lists maintain the order of elements, whereas sets do not.
# Duplicates: Lists can have duplicate elements, but sets cannot.
# Performance: Sets are generally faster than lists for membership testing and other operations due to their underlying hash-based implementation.

# Example Usage
# Sets are useful in scenarios where you need to manage collections of unique items, 
# perform mathematical set operations, or quickly test membership:

# Example 
# # Removing duplicates from a list
numbers  = (1,2,3,2,3,4,5,4,5,4,6,7,8,4,9,10)
# print(numbers)
# print(set(numbers)) # Output : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# Summary
# Creation: Use {} or set() to create sets.
# Characteristics: Sets are unordered collections of unique items and are mutable.
# Operations: Support union, intersection, difference, and symmetric difference.
# Methods: Include adding, removing, and various set operations.
# Comprehensions: Create sets using set comprehensions.
# Comparison: Faster for membership testing compared to lists.





# Frozen set 
# In Python, a frozenset is a built-in data type that is similar to a set 
# but with one key difference: 
# it is immutable. 
# Once a frozenset is created, its elements cannot be changed, added, or removed.

# Creating a Frozenset
# A frozenset is created using the frozenset() constructor:

# Creating a frozenset from a list
numbers = [1,2,3,4,5]
# frozenset_numbers = frozenset(numbers)
# print(frozenset_numbers) # Output : frozenset({1, 2, 3, 4, 5})
# print(type(frozenset_numbers))

frozenset1 = ({1,2,3,4,5})
# print(type(frozenset1))


# Characteristics
# Immutable: Once created, the contents of a frozenset cannot be modified.
# Hashable: Since frozensets are immutable, they can be used as keys in dictionaries or elements in other sets.
# Unordered: Like regular sets, frozensets do not maintain any order among their elements.

# Operations on Frozensets
# Accessing Elements
# Since frozensets are unordered, you cannot access elements by index. Instead, you can iterate over the elements:


frozenset1 = ({1,2,3,4,5, 6, 7, 8, 9, 10})

# for i in frozenset1:
#   print(i)
  