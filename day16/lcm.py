import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from day16.calculate_gcd import calculate_gcd




n1=int(input("Enter First Number :->"))
n2=int(input("Enter Second Number :->"))

gcd= calculate_gcd(n1,n2)

lcm = (n1*n2)//gcd
print(lcm)



