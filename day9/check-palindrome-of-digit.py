n=int(input("PLEASE ENTER A NUMBER ->"))

actualno=n

reverse_num = 0
while n > 0 :
    r = n % 10 
    reverse_num = (reverse_num*10)+r
    
    q = n//10
    n=q

if reverse_num == actualno:
 print("yes")
else:
    print("no") 