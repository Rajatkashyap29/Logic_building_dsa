arr = [-8,-3,2,5,9]
i = 0
j = len(arr)-1


min_diff = 99999999999999999999999999999999999999999999999999999999999999999999999999999999

while i < j  :
    sum = abs(arr[i] + arr [j])
    
    if sum < min_diff :
        min_diff = sum 
        print(f"Pair is {(arr[i],arr[j])}")
        i+=1
    
    if sum<0:
        i+=1
    elif sum > 0 :
        j-=1
    else:
        print(f"Pair is {(arr[i],arr[j])}")
                    