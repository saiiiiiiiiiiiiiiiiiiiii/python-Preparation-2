# 2)Decorators with Arguments:
# If you need to pass arguments to your decorator, you can use a decorator factory:

def repeat_n_times(n):
  def decorater(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
      print("Decorated function executed")
    return wrapper
  return decorater


@repeat_n_times(5)
def say_name(name):
  print(f"Hello, {name}")

say_name('Sainath')