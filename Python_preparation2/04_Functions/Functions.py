# 1)  Basic functions syntax 

# def Square(a):
#   return a * a
# print(Square(5))  # Output: 25


# 2) function with multiple parameter's 
# Create a function that takes two number's as a parameter's and return's their sum
# def add_of_two(a, b):
#   return a + b
# print(add_of_two(5, 7))  # Output: 12


# 3) Polymorphism in Function's 
# Write a Function multiply that multiplies two number's ,but can also accept and multiply string's

# def multiply(a, b):
#   return a * b

# print(multiply(5,8))            # Output: 40
# print(multiply('Sainath  ', 3)) # Output: Sainath  Sainath  Sainath  


# 4)Function Returning Multiple values
# Create a Function that return's both the area and circumfrence of a circle given its radiu

# def Area_and_Circumference_of_circle(radius):
#   area = 3.14 * radius * radius
#   circumference = 2 * 3.14 * radius
#   return area, circumference
# area, circumference = Area_and_Circumference_of_circle(5)
# print(f"Area of circle is {area} and Circumference of circle is {circumference}")
# Output: Area of circle is 78.5 and Circumference of circle is 31

# 5)Default parameter value 

# def Hello(name = None):
#   return f"Hello {name}"
# print(Hello(''))  # Output: Hello None
# print(Hello('Sainath'))  # Output: Hello Sainath

# 6)Create a lambda Function to compute a cube of a number .
# Cube = lambda x : x * x * x
# print(Cube(5))  # Output: 125

# 7) Function with args
# Write a function that takes variable  number of argument's and returns their sum  

# def sum_of_numbers(*args):
#   return sum(args)
# print(f"The Sum of Given Numbers is :{sum_of_numbers(1,2,3,4,5,6,7,8,9,10)}")


# 8)Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format 

# def print_key_Value(**kwargs):
#   for key, value in kwargs.items():
#     print(f"{key} : {value}" )
    
# print_key_Value(name = "Sainath", age = 20, gender = "Male")


# 9) Generator function with yeild 
# write a generatoe function that yeilds even number's up to a specified limit

# def even_numbers(Limit):
#   for i in range(Limit):
#     if i % 2 == 0:
#       yield i

# print(even_numbers(11))
# for i in even_numbers(11):
#   print(i)

# 10) Recursive Function
# Create a recursive function to calculate a factrial of a number

# def factorial(n):
#   if n == 1 or n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)
# print(factorial(5))  # Output: 120


