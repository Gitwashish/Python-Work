#priority queue another variation of queue, here insertion/deletion 
#can be done at last/first/or anywhere in b/w 
#priority queue is like a bada temple line for darshan priority like
# vvip > vip > Normal same concept is here
#priority == Rank ,less Rank more priority


#priority using list
class Priorityqueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1] <= priority:
            index+=1
        self.items.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)

p1=Priorityqueue()
p1.push(10,3)
p1.push("ram",4)
p1.push("syam",7)
p1.push(50,1)
p1.push("Dholkpur",5)
print(p1.size())
while not p1.is_empty():
    print(p1.pop())
print(p1.size())



