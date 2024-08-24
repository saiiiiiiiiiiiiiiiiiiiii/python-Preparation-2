class car:
  def __init__(self, brand, model):
    self.brand = brand
    self._model = model

  def full_name(self):
    return f"{self.brand} {self._model}"
  
  def get_brand(self):
    return self.brand
  
  def fuel_type(self):
    return "Gasoline"
  
  @staticmethod
  def general_description():
    return "This is a car and Cars are an important means of transport."
  
  @property
  def model(self):
    return self._model
  

class electric(car):
  def __init__(self, brand, model, battery_capacity):
    super().__init__(brand, model)
    self._battery_capacity = battery_capacity
    # self.fuel_type = "Electric"

  def fuel_type(self):
    return "Electric"
  
  def full_name(self):
    return f"{self.brand} {self._model} with {self._battery_capacity}"

  @property
  def battery_capacity(self):
    return self._battery_capacity
# my_first_car = car('TATA', 'Safari')
# print(my_first_car.brand)
# print(my_first_car.model)
# print(my_first_car.full_name())
# print(my_first_car.get_brand())
# print(my_first_car.fuel_type())
# print(car.general_description())

# my_first_car.model = 'Nexon'
# print(my_first_car.model)


# my_first_electric_car = electric('MG', 'Hector', 'Lithium Iron')
# print(my_first_electric_car.brand)
# print(my_first_electric_car.model)
# print(my_first_electric_car.battery_capacity)
# print(my_first_electric_car.full_name())
# print(my_first_electric_car.fuel_type())
# print(my_first_electric_car.general_description())

# my_first_electric_car.battery_capacity = 'jkbcfkj'
# print(my_first_electric_car.battery_capacity)



class engine:
  def engine(self):
    return "This is a car engine"
  
class battery:
  def battery(self):
    return "This is a electric car battery"

class cartwo(engine, battery):
  pass

my_second_car = cartwo()
print(my_second_car.engine())
print(my_second_car.battery())
