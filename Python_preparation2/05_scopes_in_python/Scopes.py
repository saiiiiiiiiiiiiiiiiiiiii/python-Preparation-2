username = "Sainath"

def func():
  username = 'Sai'
  return username


# print(username) # Output : By calling the username you will get the first one because it's global scoped 

# print(func())

# x = 22
# def func1(y):
#   z = x + y
#   return z

# print(func1(8))

def func3():
  global x
  x = 10
  return x


# print(func3())
# print(x) # Output : 10  # This is because we have used the global keyword inside



# Closure
# A closure is a function that has access to its own local scope, the scope of its outer
# def f1():
#   x = 10
#   def f2():
#     return x
#   return f2

# my_result = f1()
# print(my_result()) # Output : 10


def mainfunc(num):
  def actual(x):
    return x ** num
  return actual

f = mainfunc(10)
print(f(2)) # Output : 1024
