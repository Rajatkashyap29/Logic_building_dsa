# arr=[1,2,8,30,40,100]
# i=0
# map={}
# tar = 6
# while i< len(arr):
#     diff = arr[i]-tar
    
#     ans = map.get(diff,None)
#     if ans is None:
#         map[arr[i]] = i
#     else:
#         print(f"pair is {arr[i],diff}")    
    
#     i+=1

# brute force 

# arr=[1,2,8,30,40,100]
# i=0
# target = 60 
# while i < len(arr):
#     j = i+1
#     while j < len(arr):
#         if arr[j] - arr[i] == target: # j se i ko isilie minus kr rhe kyunki arr sort haai 
#             print(f"pair is {arr[i],arr[j]}") 
#         j+=1
    
#     i+=1    


# with 2 - pointer apporach 

arr=[1,2,8,30,40,100]
i=0
j=1
target = 60 

while j < len(arr):
    if arr[j]-arr[i] == target :
        print(f"pair is {arr[i],arr[j]}")
        i+=1
        j+=1
    elif arr[j] - arr[i] < target :
        j+=1
    else:
        i+=1
        if i == j:
            j+=1         
         
            
    