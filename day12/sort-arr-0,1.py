arr=[0,1,1,0,0,1,1,0,1,0,0]
i=0
count_0 = 0
while(i<len(arr)):
    if arr[i] == 0:
        count_0 = count_0 + 1
    i+=1

count_1 = len(arr)-count_0

i=0
while i< count_0 :
    arr[i] = 0
    i+=1

i=count_0
while i < len(arr):
    arr[i] = 1
    i+=1


print(arr)    



#---------------------optimized version -----------------------
arr=[0,1,1,0,0,1,1,0,1,0,0]
i = 0
j = len(arr)-1
while i < j :
    if arr[i] == 1 :
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        
        j = j-1
    else:
        i+=1



print (arr)        
            
    
                    