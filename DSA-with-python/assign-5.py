# stack-Normal
class Stack:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list)==0
    def push_item(self,data):
        return self.list.append(data)    
    def pop_item(self):
        if not self.is_empty():
            return self.list.pop() 
        else:
            raise IndexError("Stack is empty")  
    def peek_item(self):
        if not self.is_empty():
            return self.list[-1]
        else:raise IndexError("Stack is empty")
    def size(self):
        return len(self.list)

s1=Stack()
s1.push_item(10)
s1.push_item(12)
s1.push_item(28)
s1.pop_item()
print(s1.peek_item())
print(s1.size())
