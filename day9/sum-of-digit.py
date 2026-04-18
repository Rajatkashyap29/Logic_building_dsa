n=int(input("PLEASE ENTER A NUMBER ->"))
sum = 0
while n > 0 :
    r = n % 10 
    sum = sum + r
    
    q = n//10
    n=q

print ("AFTER CALCULATION SUM IS -:",sum)