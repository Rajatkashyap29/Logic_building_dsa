# arr=[1,2,1,2,0,2,0,0]
# i=0
# count_0 = 0
# count_1 = 0
# while(i<len(arr)):
#     if arr[i] == 0:
#         count_0 = count_0 + 1
#     elif arr[i] == 1 :
#         count_1 = count_1 + 1
#     i+=1
    
# count_2 = len(arr) - (count_1+count_0)  

# i = 0
# while (i<count_0):
#     arr[i] = 0
#     i+=1

# i = count_0    
# while (i<(count_0  + count_1)) :
#     arr[i] = 1
#     i+=1

# i = count_0+count_1
# while( i< len(arr)):
#     arr[i] = 2
#     i+=1
    
    
# print(arr)    





#-----------------Optimized version ---------------------
arr=[1,1,2,2,0,0,1,0,2,2,2,2,1,0,2,2,0,2]
i=0
j=0
k=len(arr)-1
while(j<k):
    if arr[j] == 0:
        t=arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i+=1

        
    elif arr[j] == 1 :
        j+=1
    else :
        t = arr[j]
        arr[j] = arr[k]
        arr[k] = t
        k-=1              
        
    

print(arr)