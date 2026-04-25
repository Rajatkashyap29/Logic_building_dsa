import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from day16.calculate_gcd import calculate_gcd



n1=int(input("Enter First Number :->"))
n2=int(input("Enter Second Number :->"))

ans =  calculate_gcd(n1,n2)
print(ans)
        