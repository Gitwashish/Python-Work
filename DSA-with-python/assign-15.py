#pririty using SLL
class Node:
    def __init__(self,item=None,next=None,priority=None):
        self.item=item
        self.next=next
        self.priority=priority
class Priorityqueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def push(self,data,priority):
        n=Node(data,None,priority)
        if not self.start or priority < self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next !=None and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
    def is_empty(self):
        return self.start==None
    def pop(self):
        if self.is_empty():
            raise IndexError("priority is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data    
    def size(self):
        return self.item_count

p1=Priorityqueue()
p1.push("Amit",3)
p1.push(10,2)
p1.push("ram",4)
p1.push("syam",7)
p1.push(50,1)
p1.push("Dholkpur",5)
while not p1.is_empty():
    print(p1.pop())


        