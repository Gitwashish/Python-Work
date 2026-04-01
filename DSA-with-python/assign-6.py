#stack-using List as parent class
class Stack(list):   #stack class(child class)inherited all propertries/method of list class(parentclass)
    def is_empty(self):
        return len(self)==0     #self is object of stack class
    def push_item(self, data):
        self.append(data)
    def pop_item(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")  
    def peek_item(self):
        if not self.is_empty():
           return self[-1]      
        else:
            raise IndexError("Stack is empty")     
    def size(self):
        return len(self)

    def insert(self, index, data):   #data stack can't be inserted in stack 
        raise AttributeError("No attribute 'insert' in Stack")             
            
s1=Stack()
# s1.insert(0,10)   can't be done b'coz of overriding
s1.push_item(20)
s1.push_item(30)    #top value
print(s1.peek_item())




