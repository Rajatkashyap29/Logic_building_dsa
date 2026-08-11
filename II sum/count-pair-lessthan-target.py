arr = [2,4,6,3,10,0,9,8,1]

target = 6
i=0
count = 0
while i < len(arr):
    j = i+1
    while j < len(arr):
        if arr[i] + arr[j] <= target :
            count = count+1
            break
        else:
            j+=1
    
    i+=1
    
print(count)        

    

arr = [5,6,7,8,9,10]
target = 16

arr.sort()

i = 0
j = len(arr) - 1
count = 0

while i < j:
    if arr[i] + arr[j] < target:
        count += j - i
        i += 1
    else:
        j -= 1

print(count)