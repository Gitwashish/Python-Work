class Car:
    # brand = None
    # model = None

    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car +=1
    def Full_name(self):  #ading functionality
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):  #exmple of Polymorphism
        return "petrol or Diesel"

    
class ElectricCar(Car): #this is inherited class attribute
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size    
    
    def fuel_type(self):
        return "Electric charge"
    
safari = Car("Tata", "Safari")
mahendra = Car("Mahendra", "xuv300")
# print(safari.total_car)
print(Car.total_car)





# print(safari.fuel_type())

# my_tesla = ElectricCar("Tesla", "model S", "85KWH")
# print(my_tesla.fuel_type())

# print(my_tesla.brand)
# print(my_tesla.battery_size)
# print(my_tesla.Full_name())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)    
# print(my_car.model)
# print(my_car.Full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
