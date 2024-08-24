# In Python, Lists are one of the most versatile and commonly used data types. They 
# Ordered collections that can hold a variety of items. Here's a detailed look at 
# how lists work in Python 

# Creating Lists 
# Lists are created using square brackets [] with elements separated by commas:
empty_list = []

# Creating a List with an elements 
fruits = ['apple', 'bananna', 'cherry']

# Lists can contain different types of an element 
mixed_list = [1, 'Hello', 3.14, [1,2,3]]
# print(mixed_list)

# Accessing Elements 
# Lists are Indexed, meaning each element has a position starting from 0:
fruits = ['apple', 'bananna', 'cherry']

# Accessing Elements 
print(fruits[0])
print(fruits[1])
print(fruits[2])

# # Negative indexing accesses elements from the end
print(fruits[-1])


# Slicing Lists
# You can get a subset of a list using slicing:

fruits = ['apple', 'bananna', 'cherry', 'date', 'elderberry']
# slicing from  index 1 to 3
subset = fruits[1:3]
print(subset)


# Modifying Lists
# Lists are mutable, meaning you can change their content:
fruits = ['apple', 'bananna', 'cherry']
print(fruits)
# Changing an element 
fruits[1] = "Ananas"
print(fruits)
# Adding elements 
fruits.append('Date') # Adds an element to the end 
print(fruits)

# Inserting elements 
fruits.insert(1, 'avocado') # Inserts avacado at index 1 
print(fruits)

# Removing elements
# print(fruits.remove('bananna')) # Removes the first Occurence of Banana
print(fruits.pop())


# List Operations 
# Concatenation 
# You can concatenate lists using the + operator:
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9,10]
print(list1 + list2)

# Repetition
# You can repeat lists using the * operator:
list3 = [1,2,3,4,5]
print(list3 * 3)


#  List Methods 
# Python lists have several built-in methods for manipulation:
# Adding Elements
fruits = ['apple', 'Bananna']
fruits.append('cherry')
print(fruits)
fruits.extend(['Date', 'Elderberry'])
print(fruits)

# Inserting Elements 
fruits.insert(1, 'Ananas')
print(fruits)

# Removing Elements 
fruits.remove('Bananna')
print(fruits)
# if 'Bananna'  in fruits:
#   print("Item is there!")
# else:
#   print("Item is not there ")

# Sorting and Reversing 
numbers = [1,6,4,7,8,9,3,2,4,6]
numbers.sort() #.sort() Method used to sort the list from small to big
print(numbers) 
numbers.sort(reverse=True) #.sort() Method used to sort the list from big to small
print(numbers)

fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')  # Output: 1
count = fruits.count('apple')  # Output: 1
print(index)
print(count)

# List Comprehensions
# List comprehensions provide a concise way to create lists:
# creating a list of Squres
Squares = [x ** 2 for x in range(1, 11)]
print(Squares)

# Conditionals list Comprehensions 
even_squares = [x ** 2 for x in range(0, 11) if x % 2 == 0]
print(even_squares)


# Nested Lists
# Lists can contain other lists, which allows for the creation of multi-dimensional data structures:

matrix = [
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15]
]
print(matrix[1][3])