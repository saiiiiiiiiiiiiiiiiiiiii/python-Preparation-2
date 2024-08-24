# 7) Static Method
# Add a static Method to the car Class that return's a general desciription of car 


class car:
  total_car = 0
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    car.total_car += 1

  def full_name(self):
    return f"{self.brand} {self.model}"
  
  def get_brand(self):
    return self.brand
  
  def fuel_type(self):
    return "Gasoline"
  @staticmethod # This is Decorator's in python @ when we use a keyword "@staticMethod" then we don't need to use the self keyword in the placeholder
  def General_Description():
    # return  "This is a", {self.fuel_type()} ,"car, made by", {self.brand}
    # return f"This is a {self.fuel_type()} car made by {self.brand}"
    return "Car are means of transport"

  

myfirst_car = car('Tata', 'Safari')
print(myfirst_car.full_name()) # Output: Tata Safari
print(myfirst_car.get_brand())  # Output: Tata
print(myfirst_car.fuel_type())  # Output: Gasoline 
print(car.total_car) # Output: 1

class electric(car):
  def __init__(self, brand, model, battery_capacity):
    super().__init__(brand, model)
    self.battery_capacity = battery_capacity
    # car.total_car =+ 1

  def fuel_type(self):
    return 'electric'



my_first_electric_car = electric('MG', 'Hector', 'Iron Lithium Battery')
print(my_first_electric_car.full_name()) # Output: MG Hector
print(my_first_electric_car.get_brand())  # Output: MG
print(my_first_electric_car.fuel_type()) # Output : electric
print(car.total_car) # Output: 2
print(my_first_electric_car.General_Description())