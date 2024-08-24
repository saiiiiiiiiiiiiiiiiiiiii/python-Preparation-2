# 2) Class Method and Self
# Add a Method to the Car Class That displays the full name of the car


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return  f"{self.brand} {  self.model}"
    

my_first_car = Car('TATA', 'Safari')
print(my_first_car.brand)
print(my_first_car.model)
print(my_first_car.full_name())
