#concept of overriding

class Vehicle:             #parent class   #class is blue-print of object
    def __init__(self,milege,cost):
        self.milege=milege
        self.cost=cost
    def show_vehicle_detail(self):
        print("cost of vehicle is:", self.cost)
        print("Milege of vehicle is:", self.milege)

# v1 =Vehicle(25,450000)               #object is instance of class
# v1.show_vehicle_detail()               


class Car(Vehicle):                #car is child class of vehicle class
    def __init__(self,milege,cost,tyre,hp):
        super().__init__(milege,cost)
        self.tyre=tyre
        self.hp=hp
    def show_car_detail(self):
        print("Milege of the car is:",self.milege)    
        print("cost of the car is:",self.cost)    
        print("tyre type of the car is:",self.tyre)    
        print("Horse power of the car is:",self.hp)    


c1=Car(30,50000,"CEAT-tyres",2000)
c1.show_car_detail()
