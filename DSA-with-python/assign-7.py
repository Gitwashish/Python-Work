#stack- using linkedlist as parent class
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0    #in stack inserting and pulling from 
    def is_empty(self):       #between is not possible, only from 
        return self.start==None    #start or end
    def push(self,data):
        n=Node(data,self.start)    
        self.start=n
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next    
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")

    def peek_item(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()
    def size(self):
        return self.item_count
    
s1=Stack()
s1.push(10)    
s1.push(20)    
s1.push(30)
print("total item in stack",s1.size())    
print("top element on the stack is",s1.peek_item())
print("poped element is",s1.pop())
print("top elemnt in stack is",s1.size())
print("top elemnt in stack is",s1.peek_item())
print()





