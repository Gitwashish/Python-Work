class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
class DLL:
    def __init__(self, start=None):  #setting  environment
        self.start = start
    def is_empty(self):  #check/doing dll class list is empty or not
        return self.start==None   
    def insert_at_start(self, data):
        n =Node(None, data, self.start) #new node created
        self.start.prev=n
        self.start = n  #containg with head/start
    def insert_at_last(self, data):
        n =Node(self.start, data, None)
        if self.is_empty():
            self.start = n
            n.next=None  #this line is bydefault applied if not written
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            else:
             self.start = n 
        
              
 