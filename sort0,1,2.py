arr = [0,0,1,2,1,2,2,1,0,0,1,2,0,1,2]

i = 0
j = 0
k = len(arr)-1

while j < k:
    if arr[j] == 0 :
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
        i+=1
        j+=1
    if arr[j] == 1 :
        j+=1
    if arr[j] == 2:
        temp = arr[k]
        arr[j] = arr[k]
        arr[k] = arr[j]
        k-=1
print(arr)        
                  

