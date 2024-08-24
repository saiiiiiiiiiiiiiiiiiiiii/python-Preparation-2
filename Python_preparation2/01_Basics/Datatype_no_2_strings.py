#  Strings in Python are Fundamental datatype used to represent text. They are 
#  Sequences of characters enclosed in Quotes. 
# Here's a detailed look at how strings work in python

# Creating Strings 
# You can create strings using single quotes, double quotes, or triple quotes:
single_quotes_str = 'Hello, World!'
double_quotes_str = "Hello, World!"
triple_quotes_str = '''Hello, World!'''

# string Operations 
# 1) Concatenation 
# You can concatenate strings using the + operator:
str1 = 'Hello'
str2 = "world"
print(str1 + ", ",str2)

# 2) Repetition 
# You can repeat a string using the * operator:
str = 'Hello  '
print(str * 3)

# 3) Indexing and Slicing 
# Strings are indexed, meaning you can access individual characters using square brackets []:
str = 'Hello, World!'
print(str[0])  # prints H
print(str[-1]) # prints !
# You can also slice strings to get a subset of characters:
print(str[0:5])  # prints Hello


#  4) Length 
# To get the length of a string (the number of characters), use the len() function:
to_identify_the_length_of_string = "Sainath" 
print(len(to_identify_the_length_of_string))


# String Methods 
# Strings come with a variety of built-in methods for manipulation:

# Case Conversion
Case_conversion = 'Sainath'
print(Case_conversion.upper()) # prints SAINATH
print(Case_conversion.lower()) # prints sainath
print(Case_conversion.capitalize()) # prints Sainath
print(Case_conversion.title()) # prints Sainath


# Stripping Whitespace
# You can remove leading and trailing whitespace from a string using the strip() method:
Removing_whitespace_from = "     sainath        "
print(Removing_whitespace_from)
print(Removing_whitespace_from.strip())

# Splitting and Joining
# You can split a string into a list of substrings using the split() method:
splitting_string_into_list = "sainath is a python developer"
print(splitting_string_into_list.split())
# You can join a list of strings into a single string using the join() method:
join_string_into_single =(["sainath", "is", "a", "python", "Developer"])
print(" ".join(join_string_into_single))


# Finding and Replacing
text = 'Python is a Great'.lower()
print(text.find('great')) # Find() Method uses to find the word 
print(text.replace('great', 'good')) # replace() method uses to replace the word
print(text)


# Checking for Substrings
checking_string = "Python is Great "
print('Great' in checking_string)


# Formatting Strings
# You can format strings using f-strings (formatted string literals) or the format() method:
name = 'Alice'
age = 30
formatted_str = f'Name: {name}, Age: {age}'  # Output: 'Name: Alice, Age: 30'
# print(formatted_str)

# format() Method
formatted_str1 = 'Name: {}, Age: {}'.format(name, age)  # Output: 'Name: Alice, Age: 30'
print(formatted_str1)