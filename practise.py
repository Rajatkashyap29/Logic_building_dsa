arr=[10,23,42,1,65,32,90,11,32,54]


largest = 0
secondlargest = 0 

i = 0

while (i < len(arr)):
    if arr[i] > largest:
        secondlargest = largest
        largest = arr[i]
        
    elif arr[i] > secondlargest and arr[i] != largest :
        secondlargest = arr[i]
   
    i+=1 


print(secondlargest)    
        
            