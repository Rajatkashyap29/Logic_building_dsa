class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self,d):
        n = Node(d)
        
        if self.head == None:
            self.head=n
        else:
            temp = self.head
            
            while temp.next != None:
                temp = temp.next
            temp.next = n
    
    
    def display(self):
        i = self.head
        
        while i != None:
            print(F"Your Data Is {i.data}")
            
            i = i.next    
    
    def insert_node_at_starting(self,d):
        new_node = Node(d)
        new_node.next = self.head
        self.head = new_node
        print(f"{d} Added SucessFully")
    
    def insert_node_at_last(self,d):
        temp = self.head
        while temp.next != None :
            temp = temp.next
       
        new_node = Node(d)
        temp.next = new_node
        print(f"{d} Added SucessFully")
        
        
    def insert_node_at_specific_position(self,d):    
        element = int(input("Please Enter Position You Want To Inser Data"))
        i = 0
        temp = self.head
        while i < (element-2) :
            temp = temp.next
            i+=1
        new_node = Node(d)
        temp.next = new_node.next
        new_node.next = temp.next
        print(f"{d} Added SucessFully")
    
    def delete_at_starting(self):
        self.head = self.head.next
    
    
    def delete_at_last(self):
        temp = self.head
        while temp.next != None and temp.next.next != None:
            temp = temp.next
            
        temp.next = None
        
        if temp == self.head:
            self.head = None    
        

             
        
                
                
                
        
                
        
        
        
        
kukur = LinkedList()
kukur.insert(10)
kukur.insert(11)
kukur.insert(12)
kukur.insert(13)
kukur.display()
