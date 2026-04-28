class LTCompany :
    r = 5
    count=0
    def __init__(self,x,y):
        self.p = x
        self.t = y
        LTCompany.count +=1
   
    def calculate_si(self):
        s = (self.p*self.t*LTCompany.r) // 100
        
        return s
  
    @classmethod
    def print_interest(cls):
        print(LTCompany.r)
        

print(LTCompany.count)  
    
ram = LTCompany(500,5)
shyam1 =LTCompany(10000,5)
shyam2 =LTCompany(10000,5)
shyam3 =LTCompany(10000,5)

print(LTCompany.count)  
shyam4 =LTCompany(10000,5)
shyam5 =LTCompany(10000,5)
shyam6 =LTCompany(10000,5)

print(LTCompany.count)  

x= ram.calculate_si()
y = shyam1.calculate_si()



# print(x,y)
  
                      
    