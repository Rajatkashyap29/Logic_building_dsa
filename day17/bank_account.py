# class BankAccount:
#     def __init__(self,name,balance):
#        self.name = name 
#        self.balance = balance
    
#     def deposit(self,amount):
#         self.balance += amount
#         print(f" Amount INR {amount} deposit in HDFC BANK ACC-NO : XXXXXXXXX8123 ACC Holder NAME {self.name} AND total balance is {self.balance}")
    
    
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("insufficent balance ")
        
#         else:
#             self.balance -= amount    
#             print(f"{amount} withdraw total remain balance is {self.balance}")
            
# acc1 = BankAccount("Ram",50000)
# acc2 = BankAccount("shyam",50000)
# acc3 = BankAccount("mohan",50000)

# acc1.deposit(1222)
# acc1.withdraw(51220)



class Student :
    
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = roll 
        self.marks = marks
        
    def Passed_student(self):
        if self.marks > 30 :
            print(f"congratulation student: {self.name} is pass") 
        else :
            (f"sorry student :{self.name} Better Luck Next time ")  


s1 = Student("rajat",12,32) 
s1.Passed_student()                