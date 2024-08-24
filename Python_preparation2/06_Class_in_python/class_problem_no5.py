# Polymorphism
# Demonstrate polymorphism by defining a method fuel_type in both Car and Electric_Car 
# classes , but with different behaviour's

class car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"
  
  def get_brand(self):
    return self.brand
  
  def fuel_type(self):
    return "Gasoline"
  

class electric(car):
  def __init__(self, brand, model, battery_Capacity):
    super().__init__(brand, model,)
    self.battery_Capacity = battery_Capacity

  def fuel_type(self):
    return "Electric"





my_first_car = car('Tata', 'Safari')
print(my_first_car.full_name())  # Outputs: Tata Safari
print(my_first_car.get_brand())  # Outputs: Tata
print(my_first_car.brand)        # Outputs: Tata
print(my_first_car.model)        # outputs: Safari
print(my_first_car.fuel_type())  # Outputs: Gasoline



# my_first_electric_car = electric('Tata', 'Nexon', 'Iron Lithium Battery')
# print(my_first_electric_car.full_name())  # Outputs: Tata Nexon
# print(my_first_electric_car.get_brand())  # Outputs: Tata
# print(my_first_electric_car.brand)        # Outputs: Tata
# print(my_first_electric_car.model)        # Outputs: Nexon
# print(my_first_electric_car.battery_Capacity)  # Outputs: Iron Lithium Battery
# print(my_first_electric_car.fuel_type())       # Outputs : Electric

