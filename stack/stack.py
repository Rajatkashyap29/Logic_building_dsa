class Stack :
    def __init__(self):
        self.l = []
        
    
    def length(self):
        return len(self.l)    
    
    
    def push(self,value):
        self.l.insert(0,value)
        
    def peek(self):
       if len(self.l) == 0 :
           raise Exception("stack is empty")
       else:
           return self.l[0] 
       
    def pop(self):
        if len(self.l) == 0 :
           raise Exception("stack is empty")
        else: 
           return self.l.pop(0)
           
           
           
stk = Stack() 
stk.pop()           