arr = [2,4,6,3,10,0,9,8,1]

target = 9
map = {}

i= 0
count = 0
while i < len(arr):
    ans = target-arr[i]
    
    req = map.get(ans,None)
    
    if req is None :
        map[arr[i]] = i
    else :
        count = count + 1
    
    i+=1

print(f"total pair is :",count)            