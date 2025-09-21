class emp:
    def __init__(self,name,email):
        self.email=email
        self.name=name
    def display(self):
        print("details of emp are:",self.name,self.email)    


t1=emp('ram','ram@gmail')
t1.display()

