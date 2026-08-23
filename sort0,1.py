arr = [0,1,1,1,0,0,1,0,0,1,0,0]

i = 0
j = len(arr)-1

while i < j :
    if arr[i] == 0 :
        i+=1
    else:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j]  = temp
        j-=1

print(arr)                   