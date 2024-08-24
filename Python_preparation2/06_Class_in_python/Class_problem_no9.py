# 9) Class inheritence and isinstacnce () Function
# Problem Demonstrate the use of instance() to check if my_tesla is an instacnce of Car and Electric Car


class car:
  def __init__(self, brand, model):
    self.brand = brand
    self._model = model


  def full_name(self):
    return f"{self.brand} {self._model}"

  def fuel_type(self):
    return "Gasoline"
  
  def get_brand(self):
    return self.brand
  


  @staticmethod
  def general_description():
      return "This is a car and car is a important means of transport"
  
  @property
  def model(self):
    return self._model

  def full_detail(self):
    return f"Brand: {self.brand}, Model: {self._model}, Fuel Type:"
  

class electric(car):
  def __init__(self, brand, model, battery_capacity):
    super().__init__(brand, model)
    self.battery_capacity = battery_capacity


  def fuel_type(self):
    return 'Electric'

  def full_detail(self):
    return f"{self.full_name()} with a battery capacity of {self.battery_capacity}"

my_first_car = car('Mahindra', 'evirtoo')
print(my_first_car.brand)
print(my_first_car.model)
print(my_first_car.full_name())
print(my_first_car.fuel_type())
print(my_first_car.general_description())
print(my_first_car.get_brand())
print(my_first_car.full_detail())
print(isinstance(my_first_car, car))
print(isinstance(my_first_car, electric))





# my_first_electric_car = electric('Mahindra', 'eXUV500', 'Lithium - iron')
# print(my_first_electric_car.brand)
# print(my_first_electric_car.model)
# print(my_first_electric_car.battery_capacity)
# print(my_first_electric_car.full_detail())
# print(isinstance(my_first_electric_car, car))
# print(isinstance(my_first_electric_car, electric))

# my_first_electric_car.model = 'evirto'   # AttributeError:  property 'model' of 'electric' object has no setter you will still get this error if you try to make a change in the model name because it's been inherirted by Car class
    