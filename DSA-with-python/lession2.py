#concept of Inheritance..

#1.multiple inheritance
class Parent1:
    def get_name1(self,name1):
        self.name1=name1
    def show_name1(self):
        return self.name1

# p1=Parent1()
# p1.get_name1("Ramesh")
# print(p1.show_name1())

class Parent2():
    def get_name2(self,name2):
        self.name2=name2
    def show_name2(self):
        return self.name2
    
# p2=parent2()
# p2.get_name2("Pranjal")
# print(p2.show_name2())

class Derived(Parent1,Parent2):
    def get_name3(self,name3):
        self.name3=name3
    def show_name3(self):
        return self.name3  

# d1=Derived()
# d1.get_name1("Ramesh")      
# d1.get_name2("Pranjal")      
# d1.get_name3("Shrivastam") 
# print(d1.show_name1())     
# print(d1.show_name2())     
# print(d1.show_name3())     


#2.multiple level inheritance

class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
# p1=Parent()
# p1.get_name("Rakesh")
# p1.show_name()        

class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        print(self.age)
# c1=Child()
# c1.get_age(39)
# c1.show_age()

class grandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        print(self.gender)
# gc=grandChild()
# gc.get_name("Rakesh")
# gc.get_age(39)
# gc.get_gender("Male")
# gc.show_name()        
# gc.show_age()        
# gc.show_gender()        










