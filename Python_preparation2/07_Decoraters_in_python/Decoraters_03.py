# 3) Decorators with Arguments and Return Values:
# If the decorated function takes arguments and returns a value, the wrapper needs to handle these appropriately:

def my_decorater(func):
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    print(f"The Function {func.__name__}() with the args: {args} and kwargs: {kwargs} and the result: {result}")
    return result
  return wrapper


@my_decorater
def sum_of_two(x, y):
  return x + y

sum_of_two(5,5)

