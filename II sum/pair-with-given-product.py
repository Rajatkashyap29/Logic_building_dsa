arr=[10,2,5,6,8,9,7,3,4,12]
arr.sort()
target = 60
i = 0 


while i < len(arr):
    j = i+1
    while j < len(arr):
        if (arr[i] * arr[j]) == target :
            print(f"pair is ({arr[i],arr[j]})")
        j+=1
    i+=1
    



                  
    