arr = [1,1,1,1,2,2,2,3,3,4,4,5,5,5]

i = 0
j = 1

while j < len(arr):
    if arr[i] == arr[j] :
        j+=1
    else:
        i+=1
        arr[i] = arr[j] 
        


print(i+1)
