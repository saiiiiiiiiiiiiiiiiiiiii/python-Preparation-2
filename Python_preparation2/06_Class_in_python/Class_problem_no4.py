# Encapsulation
# Modify The Car class to encapsulate the brand attribute making it private and provide a getter method for it

class car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"
  
  def get_brand(self):
    return self.brand
  
class electric(car):
  def __init__(self, brand, model, battery_capacity):
    super().__init__(brand, model)
    self.battery_capacity = battery_capacity

my_first_car = car('Tata', 'Safari')
print(my_first_car.full_name())  # Outputs: Tata Safari
print(my_first_car.get_brand())



my_first_Electric_car = electric('MG','Hector', 'Iron Litihium Battery')
print(my_first_Electric_car.full_name())  # Outputs: MG Hector
print(my_first_Electric_car.battery_capacity)  # Outputs: Iron Litihium Battery
print(my_first_Electric_car.get_brand())
