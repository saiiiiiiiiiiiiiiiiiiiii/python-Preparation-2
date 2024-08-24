from functools import wraps

def decorater(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    print(f"Result: {result}")
    return result
  return wrapper


@decorater
def say_hello(name):
  '''This is my docstring i can access it by using wraps from functools'''
  return f"Hello {name} !"


say_hello('Sainath')

print(say_hello.__doc__)
print(say_hello.__name__)