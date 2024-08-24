# How Decorators Work
# Basic Function Decorator:
# Here's a simple example of a decorator that logs the execution of a function:

def decorater(func):
  def wrapper():
    print('Something is happening before the function calling')
    func()
    print('Something is happening after the function calling')
  return wrapper


@decorater
def say_Hello():
  print('Hello')

say_Hello()