# Dictionaries in Python are a versatile and powerful data type used to store key-value pairs.
# They are unordered collections, meaning that the items have no specific order. 
# Here’s a detailed explanation of how dictionaries work in Python:

# Creating Dictionaries 
# Dictionaries are created using curly braces {} with key-value pairs.
# Separated by colons : and pairs separated by commas:
# Creating an Empty Dictionary 
empty_dict = {}
# print(empty_dict)  # Output: {}

# Creating a Dictionary with an element 
dict_with_element = {"name": "John", "age": 30, "City" : "New York"}
# print(dict_with_element)  # Output: {'name': 'John', 'age': 30, "City" : "New York"}

# Accessing Values
# You can access values in a dictionary using their keys:
person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}
# print(person)
# print(person["Name"]) # Output : Sainath
# print(person["Age"]) # Output : 25
# print(person["City"]) # Output : Bangalore



# Adding and Updating Items
# You can add new key-value pairs or update existing ones:

person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}

# person["Name"] = 'Sai'
# print(person)
# person["Age"] = 21
# print(person)
# person["City"] = 'Thane'
# print(person)


# Removing Items
# Items can be removed using the del statement or the pop() method:
person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}
del person["City"]  # with the help of the del keyword you can delete the key:value pair from the dictionary 
# print(person)
# print(person.pop('Age')) # pop() Method deletes the value and return it 

# Dictionary Methods
# Dictionaries have several useful methods:


# values()
# Returns a view object of the dictionary’s values:
person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}
# val = person.values()       # Output : dict_values(['Sainath', 25, 'Bangalore'])
# print(val)
# print(person.values())      # Output : dict_values(['Sainath', 25, 'Bangalore'])


# keys()
# Returns a view object of the dictionary’s keys:


person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}

key = person.keys()    # Output : dict_keys(['Name', 'Age', 'City'])
# print(key)
# print(person.keys())   # Output : dict_keys(['Name', 'Age', 'City'])


# items()
# Returns a view object of the dictionary’s key-value pairs:
person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}

# print(person.items()) # Output: dict_items([('Name', 'Sainath'), ('Age', 25), ('City', 'Bangalore')])


# get()
# Returns the value for a given key, or a default value if the key is not found:
# print(person.get('Name', 'Unknow')) # Output: Sainath
# print(person.get('Height', 'Unknow')) # Output: Unknow


# popitem()
# Removes and returns the last key-value pair as a tuple:

# print(person.popitem())
# Output: ('City', 'Bangalore')
# print(person)

# clear()
# Removes all items from the dictionary:

# person.clear()
# print(person)

# Dictionary Comprehensions
# Similar to list comprehensions, dictionary comprehensions provide a concise way to create dictionaries:
Squares = {x : x ** 2 for x in range(11)}
# print(Squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# Nested Dictionaries
# Dictionaries can contain other dictionaries, allowing for complex data structures:
school = {
  "student1" : {"Name" : "Sainath", "Age" : 21, "City" : "Thane"},
  "student2" : {"Name" : "Shraddha", "Age" : 19, "City" : "Balkum"}

}
# Accessing nested dictionary values
print(school["student1"]["Name"])

# Keys and Values
# Keys: Must be immutable types (e.g., strings, numbers, tuples) and must be unique within a dictionary.
# Values: Can be any type and can be duplicated.

# Checking Membership
# You can check if a key exists in a dictionary using the in keyword:
school = {
  "student1" : {"Name" : "Sainath", "Age" : 21, "City" : "Thane"},
  "student2" : {"Name" : "Shraddha", "Age" : 19, "City" : "Balkum"}

}
checking_key_value_pairs_in_dict = 'student2' in school
print(checking_key_value_pairs_in_dict)

# Iterating Through Dictionaries
# You can iterate through the keys, values, or key-value pairs of a dictionary:
person = {
  "Name" : "Sainath",
  "Age" : 25,
  "City" : "Bangalore"
}
# Iterating through keys
for key in person:
  print(key)

for i in person.keys():
  print(i)

for j in person.values():
  print(j)

for i,j in person.items():
  print(f"{i} : {j}")


# Summary
# Creation: Dictionaries are created with {} and key-value pairs.
# Access: Values are accessed using keys.
# Modification: Items can be added, updated, or removed.
# Methods: Useful methods include keys(), values(), items(), get(), pop(), and popitem().
# Comprehensions: Allows concise creation of dictionaries.
# Nested Dictionaries: Can contain other dictionaries for complex data structures.
# Keys and Values: Keys must be immutable and unique, while values can be of any type.
# Membership: Check if a key exists using in.
# Iteration: Iterate through keys, values, or key-value pairs.