# The range function in Python is used to generate a sequence of numbers. 
# It's particularly useful in for-loops for iterating over a sequence of integers.
#  Here’s a detailed explanation of how the range function works:


# Basic Usage
# The range function can be called with one, two, or three arguments:

# range(stop): Generates numbers from 0 to stop - 1.

for i in range(11):
  # print(i)
  pass
# Output:
# 0
# 1
# 2
# 3
# 4

# 2) range(start, stop): Generates numbers from start to stop - 1.
      #range(start, stop - 1)
for i in range(2, 6):
  # print(i)
  pass
# Output:
# 2
# 3
# 4
# 5

# 3)range(start, stop, step): Generates numbers from start to stop - 1, incrementing by step.
for i in range(1, 10, 2):
    # print(i)
    pass
# Output:
# 1
# 3
# 5
# 7
# 9
# Parameters
# start: The starting value of the sequence. The default is 0.
# stop: The end value of the sequence (exclusive). This parameter is required.
# step: The difference between each number in the sequence. The default is 1.

# Range Object
# The range function returns a range object, which is a type of iterable in Python. Here’s how you can use it:

# r = range(6)
# print(type(r)) # Output: <class 'range'>
# print(list(r)) # Output: [0, 1, 2, 3, 4]

# Negative Step
# You can use a negative step to generate a decreasing sequence:

for i in range(5 , 0, -1):
  # print(i)
  pass
# Output:
# 5
# 4
# 3
# 2
# 1

# Converting to Other Types
# You can convert the range object to a list, tuple, or set:

r = range(5)
# print(list(r)) # Output: [0, 1, 2, 3, 4]
# print(tuple(r)) # Output: (0, 1, 2, 3, 4)
# print(set(r)) # Output: {0, 1, 2, 3, 4}

# Indexing and Length
# The range object supports indexing and finding its length:
r = range(6)
# print(list(r))
# print(r[2])   # Output: 2
# print(len(r)) # Output: 6


# Common Use Cases
# Looping Through Indices: 
# Often used in for-loops to iterate through a sequence of indices:
my_list = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(my_list)):
  #  print(my_list[i])
  pass

# Generating Sequences: 
# Useful for generating a sequence of numbers for calculations or operations:
numbers = [i * 2 for i in range(11)]
# print(numbers)
pass


# Looping with Steps: Generating sequences with a specific step:
for i in range(0, 20, 5):
  print(i)
# Output:
# 0
# 5
# 10
# 15


# Summary
# 1) Syntax: range(start, stop, step)
# 2) Immutable: The range object is immutable.
# 3) Lazy Evaluation: Efficient memory usage by generating numbers on demand.
# 4) Iterable: Can be used in loops or converted to other types.
# 5) Negative Step: Supports generating decreasing sequences.