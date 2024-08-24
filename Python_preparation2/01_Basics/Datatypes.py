# Datatypes in python 
# 1) Numeric Types 
# *) "int" Represents an integer values Examples 1, 42, -7
# *) "float" Represents floating Point Numbers (decimal Values). Example 3.14,0.001, 2.0.
# *) "Complex" : Represents complex  numbers which have a real and imaginary part examples: "1 + 2j", "-3 -4j" where -3 is real number and -4 is imaginiary number 
# z = 3 + 4j
# print(z.imag)



# 2) Text Type
# *) string (str) Represents strings (text). strings can be enclosed in single quotes 
# double quotes  or triple quotes (for multiline strings) 
# Example  "Hello, World!" , 'Hello, World!' , """This is a multiline string"""
Greetings = "Hello,  World!"
name = 'Sainath'
multiline = '''This is a 
                multiline 
                string '''
print(Greetings, name,"\n", multiline)

# 3) Sequence Type
# *) list : Represents ordered collections of items. list are mutable (can be changed) 
# Examples : [1,2,3], ['apple', 'Bananna', 'cherry']
fruits = ['apple', 'Bananna', 'cherry']
numbers = [1,2,3,4,5]
print(fruits, "\n", numbers)

# *) tuple : Represents ordered collection of items but tupples are immutable (cannot be changed) Examples:
# (1,2,3), ('apple', 'bananna', 'cherry')
tup = (1,2,3,4,5)
tup1 = ('apple', 'bananna', 'cherry')
print(tup, "\n", tup1)


# *) range() Represents an immutable sequence of numbers commonly used in loops 
# Examples : range(5), range(1,10, 2)
numbers = range(11)
print(numbers)



# 4) Mapping Type 
# *) Dictionary (dict) Represents a collection of a key value pair. Dictionaries are mutable 
# Examples : Male_Human =  {"name": "Sainath", "age": 20}
Male_Human =  {"name": "Sainath", "age": 20}
print(Male_Human)


#  Set Types 
# *) set : Represents an unordered collection of unique items. Sets are mutable (Can change it)
# Examples : {1,2,3}, {'apple', 'Bananna', 'cherry'}
unique_numbers = {1,2,3,4,5}
print(unique_numbers)
# *) frozenset : Represents an unordered collection of unique items but frozenset are immutable (can't change it)
# Examples : frozenset([1,2,3]), frozenset(['apple', 'bananna', 'cherry'])
frozen_set = frozenset([1,2,3,4,5])
print(frozen_set)

# 6) Boolean Type and None Type 
# bool: Represents boolean values, True or False
is_active = True
is_disabled = False

# 7) None Type 
#  None Type : Represents the absence of a value. The single value of this type is None
result = None