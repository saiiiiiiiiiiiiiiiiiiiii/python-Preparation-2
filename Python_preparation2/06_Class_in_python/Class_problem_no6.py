# 6) Class Variable
# Add a class variable to Car that  keeps track of the number of the cars created .

class car:
  total_car = 0
  def __init__(self, brand, model,):
    self.brand = brand
    self.model = model
    car.total_car += 1
  def full_name(self):
    return f"{self.brand} {self.model}"
  
  def get_brand(self):
    return self.brand
  
  def fuel_type(self):
    return "Gasoline"
  

  

class Electric(car):
  def __init__(self, brand, model, battery):
    super().__init__(brand, model)
    self.battery = battery

  def fuel_type(self):
    return "Electric"
  
myfirst_car = car('Tata', 'Safari')
print(myfirst_car.full_name())  # Outputs: Tata Safari
print(myfirst_car.get_brand())  # Outputs: Tata
print(myfirst_car.fuel_type())  # Outputs: Gasoline
print(myfirst_car.total_car)

myfirst_Electric_car = Electric('MG', 'Hector', 'Iron Lithium Battery')
print(myfirst_Electric_car.get_brand())  # Outputs: MG
print(myfirst_Electric_car.full_name())  # Outputs: MG Hector
print(myfirst_Electric_car.battery)      # Outputs: Iron Lithium Battery
print(myfirst_Electric_car.fuel_type())  # Outputs: Electric
print(myfirst_Electric_car.total_car)
