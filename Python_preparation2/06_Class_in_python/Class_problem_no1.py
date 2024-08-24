# 1) Basic class and object 
# create a car class with attributes like brand and model Then create an instance of the class 

class Car:
  def __init__(self, brand, model):
    self.brand = brand # This is attribute
    self.model = model # This is attribute

my_first_car = Car('TATA', 'Safari') # This is Instance1 (Object 1)
print(my_first_car.brand)
print(my_first_car.model)


my_second_car = Car('Suzuki', 'Maruti')  # This is Instance2 (Object 2)
print(my_second_car.brand)
print(my_second_car.model)

