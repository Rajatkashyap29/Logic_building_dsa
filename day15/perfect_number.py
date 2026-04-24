n = int(input("Please Enter A Number ->"))
i = 1
count = 0
while (i<n):
    if n % i == 0:
        count = count + i
        
    i+=1
if count == n :
    print("Yes ", n ,"is perfect ")
      
else :
    print("OOps !!  Please enter another number")           