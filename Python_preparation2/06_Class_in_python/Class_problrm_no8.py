# 8) Property Decorator's 
# Use a property decorator in the Car class to make the model attribute read_only 

class car:
  total_instance = 0
  def __init__(self, brand, model):
    self.brand = brand
    self._model = model   # By giving  underscore we make the attribute into private attibute and after making that change do that similar change to the places where model attribute turns red.
    car.total_instance += 1

  def full_name(self):
    return f"{self.brand} {self._model}"
  
  def fuel_type(self):
    return "Gasoline"
  
  def get_brand(self):
    return self.brand
  
  @staticmethod
  def general_description():
    return "This is a car and car are means of transport!."

  @property
  def model(self):
    return self._model
class electric(car):
  def __init__(self, brand, model, battery_capacity):
    super().__init__(brand, model)
    self.battery_capacity = battery_capacity

  def fuel_type(self):
      return "Electric"
  

my_first_car = car('Tata', 'Safari')
print(my_first_car.brand)
print(my_first_car.model)
print(my_first_car.full_name())
print(my_first_car.fuel_type())
print(my_first_car.get_brand())
print(my_first_car.general_description())



my_first_electric_car = electric('Mahindra', 'eXUV300', 'Lithium-ion')
print(my_first_electric_car.brand)
print(my_first_electric_car.model)
print(my_first_electric_car.battery_capacity)
print(my_first_electric_car.fuel_type())
print(my_first_electric_car.general_description())
print(my_first_electric_car.full_name())
# my_first_electric_car.model = 'evirto'
# print(my_first_electric_car.model)
print(my_first_electric_car.total_instance)