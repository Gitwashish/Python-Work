class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next
class CDLL:
    def __init__(self,start=None):
        self.start=start 
    def is_empty(self):     #give either T/F
        return self.start==None
    def insert_at_start(self, data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:    
            n.next = self.start
            self.start.prev.next = n
            n.prev = self.start.prev
            self.start.prev = n
        self.start = n
    def insert_at_last(self, data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            self.start.prev.next=n
            n.prev=self.start.prev
            self.start.prev=n
            n.next=self.start
    def search(self, data):
        if self.is_empty():
            return None
        else:
            temp= self.start
            while temp!=self.start.prev:
                if temp.item ==data:
                    return temp       
                temp=temp.next 
            if temp.item==data:
                return data
            else:
                return None
    def insert_after(self,temp,data): #if someone say insert first it'll insert after first
        if temp is not None:          #if someone say insert last it'll insrt after last
            n=Node(data,temp.next)
            n.next= temp.next
            temp.next.prev=n
            temp.next = n
            n.prev=temp
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end='')
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end='')
                temp=temp.next  
    def delete_first(self):
        if self.start is not None:
           if self.start.next==self.start:
               self.start=None
           else:
               self.start.prev.next=self.start.next
               self.start=self.start.next    
               self.start.next.prev=self.start.prev    
    def delete_last(self):
        if self.start is not None:    
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev    
    def delete_item(self, data):
        if self.start is not None:
            temp=self.start
            if temp.item==data:
               self.delete_first()
            else:
                temp=temp.next
                while temp is not self.start:  #temp is self.start.prev
                   if temp.item==data:
                       temp.next.prev=temp.prev
                       temp.prev.next=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current ==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data

mylist = CDLL()
mylist.insert_at_start(10)    
mylist.insert_at_last(20)    
mylist.insert_at_last(30)    
mylist.insert_at_last(40)    
mylist.insert_after(mylist.search(30),35) 

for x in mylist:
    print(x, end=' ')   

print()





        
            
        

            

          
            