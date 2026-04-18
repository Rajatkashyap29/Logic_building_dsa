n=int(input("PLEASE ENTER A NUMBER ->"))
reverse_num = 0
while n > 0 :
    r = n % 10 
    reverse_num = (reverse_num*10)+r
    
    q = n//10
    n=q

print ("AFTER CALCULATION REVERSE IS -:",reverse_num)