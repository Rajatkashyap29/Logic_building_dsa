# Reverse an array
arr=[10,20,30,40,50,60,70,80,90,100]

i=0
j=len(arr)-1
while(i<len(arr)/2):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    i+=1
    j-=1
    
print("Array after revershing ",arr)

    