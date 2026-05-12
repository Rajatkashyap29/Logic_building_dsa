class Coaching:
    Coaching_name = "Bright Future Academy "
    total_student = 0
    
    def __init__(self,name,age,cource,marks):
        self.name = name 
        self.age = age 
        self.cource = cource
        self.marks = marks 
        
        
        Coaching.total_student +=1
        
    def show_res(self):
            if self.marks >=30:
                print(f"Final result of {self.name} is PASS ")
            else:
             (f"Final result of {self.name} is Fail ")


print("Coaching Name:", Coaching.coaching_name)
print("Total Students:", Coaching.total_students)

s1 = Coaching("rajat",20,"AI",89)             
s2 = Coaching("rishav",28,"ML",21)             
s3 = Coaching("ritik",24,"block-chain",23)             


s1.show_res()   
s2.show_res()         
                    
        
        
    
    
        