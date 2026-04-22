import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from day9.count_of_digit import countDigit
from day13.power import power


n=94741
actual_no = n
sum = 0
y = countDigit(n)
while n>0:
    d = n % 10 
    p = power(d,y)
    sum = sum + p
    n= n//10

if sum == actual_no :
    print ("Your Num Is Amstrong Number ")  
    
else:
    print("please enter valid number.")      
    



