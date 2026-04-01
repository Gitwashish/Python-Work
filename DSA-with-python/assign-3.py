class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

    class CLL:
        def __init__(self,last=None):
            self.last=last
        def is_empty(self):
            return self.last==None
        def insert_at_start(self, data):
            n=Node(data,None)        
            if self.is_empty():
                n.next=n
                self.last=n
            else:
                n.next=self.last.next
                self.last.next=n    
        def insert_at_last(self,data):
            n=Node(data,None)        
            if self.is_empty():
                n.next=n
                self.last=n
            else:
                # self.last.next=n
                n.next=self.last.next    
                self.last=n
        def search(self, data):
            if self.is_empty():
                return None
            else:
                temp=self.last.next 
            while temp!=self.last:
                  if temp.item==data:
                      return temp
                  temp=temp.next
            if temp.item==data:
                return data
            else:
                return None      
        def insert_after(self, temp, data):
            if temp is not None:
                n=Node(data)
                temp.next=n 
                if temp==self.last:     #temp automatically moved focus to new Node just After creation
                      self.last=n       #self.last means self(list) ka last
        def print_list(self):
            if not self.is_empty():
                temp = self.last.next
                while temp!=self.last:
                    print(temp.item, end='')
                    temp=temp.next
                print(temp.item)
        def delte_first(self):
            if not self.is_empty():
                if self.last.next==self.last:
                    self.last=None
                else:
                    self.last.next = self.last.next.next    

        def delte_last(self):
            if not self.is_empty():
                if self.last.next == self.last:
                    self.last=None
                else:
                    temp=self.last.next
                    while temp.next!=self.last:
                        temp=temp.next
                    temp.next=self.last.next
                    self.last=temp
        def delte_item(self, data):
            if not self.is_empty():
                if self.last.next==self.last:
                    if self.last.item== data:
                        self.last=None        #jo node ka data match hoga uss node ko delte karnge 
                else:
                    temp=self.last.next
                    if self.last.next.item== data:
                        self.delte_first()
                    else:
                        temp =self.last.next    
                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item== data:
                                self.delte_last()
                            break
                        if temp.next.item== data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
        def __iter__(self):
            if self.last==None:
                return CLLiterator(None)
            else:
                return CLLiterator(self.last.next)

class CLLiterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.curent ==None:
            raise StopIteration
        if self.current==self.start:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
    
        return data
cll= CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10), 50)

for x in cll:
    print(x,end='')
print()
#20 10 50 30 40
cll.print_list()
#20 10 50 30 40
                    
