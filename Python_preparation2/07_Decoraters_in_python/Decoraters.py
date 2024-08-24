# Decorators in Python are a powerful and versatile feature that allows you to 
# modify or extend the behavior of functions or methods without changing their actual code. 
# They are commonly used for tasks such as logging, access control, instrumentation, and more.


# What is a Decorator?
# A decorator is essentially a function that takes another function as its argument 
# and returns a new function that typically extends or alters the behavior 
# of the original function. Decorators are often used to "wrap" a function 
# to add some functionality before or after its execution.


# How Decorators Work
# Basic Function Decorator:
# Here's a simple example of a decorator that logs the execution of a function:

# def My_Decorater(func):
#   def wrapper():
#     print("Something is happening before the function is called.")
#     func()
#     print("Something is happening after the function is called.")
#   return wrapper


# @My_Decorater   # This is how you can call the Decorater this is the syntax 
# def say_Hello():
#   print("Hello!")

# say_Hello()


# 2)Decorators with Arguments:
# If you need to pass arguments to your decorator, you can use a decorator factory:

# def Decorater(func):
#   def wrapper(*agrs, **kwargs):
#     func(*agrs, **kwargs)
#   return wrapper
# @Decorater
# def say_Hello(name):
#   print(f"Hello {name}")
# say_Hello("Sainath")


# def repeat(n):
#   def Decorater(func):
#     def wrapper(*args, **kwargs):
#       for i in range(n):
#         func(*args, **kwargs)
#     return wrapper
#   return Decorater

# @repeat(5)
# def say_Hello(name):
#   print(f"Hello {name}")

# say_Hello("Sainath")


# 3) Decorators with Arguments and Return Values:
# If the decorated function takes arguments and returns a value, the wrapper needs to handle these appropriately:


# def debug(func):
#   def wrapper(*args, **kwargs):
#     result = func(*args, **kwargs)
#     print(f"The Result is {result} of the Function {func.__name__}() with the Arguments {args} and the Keyword argument {kwargs}")
#     return result
#   return wrapper

# @debug
# def sum_of_two(a, b):
#   return a + b

# print(sum_of_two(5, 7))



# 4) Using functools.wraps:
# When you create a decorator, it’s good practice to use functools.wraps to ensure that the wrapper function retains the original function’s metadata:

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


@my_decorator 
def say_Hello(name):
  '''Hello My Name is Sainath And I am writing the doc string'''
  print(f"Hello {name}")

say_Hello("Sainath")

print(say_Hello.__name__)
print(say_Hello.__doc__)