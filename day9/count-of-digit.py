n=int(input("PLEASE ENTER A NUMBER ->"))
count = 0
while n > 0 :
    count = count + 1
    
    q = n//10
    n=q

print ("AFTER CALCULATION COUNT IS -:",count)