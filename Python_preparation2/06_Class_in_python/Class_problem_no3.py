# 3) Inheritence
# Create an Electric Class that inherits from the Car Class and has an additional attribute 

class car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"
    

class electric(car):
  def __init__(self, brand, model, battery_capacity):
    super().__init__(brand, model)
    self.battery_capacity = battery_capacity

myfirst_Car = car('Tata', 'Safari')
print(myfirst_Car.full_name())  # Output: Tata Safari


myfirst_Electric_Car = electric('Tata', 'Nexon', 'Lithium iron battery')
print(myfirst_Electric_Car.full_name())  # Output: Tata Nexon
print(myfirst_Electric_Car.battery_capacity)  # Output: Lithium iron battery
print(myfirst_Electric_Car.brand)             # Output: Tata
print(myfirst_Electric_Car.model)             # Output: Nexon          