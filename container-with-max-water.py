arr = [1,8,6,2,5,4,3,8,7]
# ans = 0
# i = 0
# while i < len(arr):
#     j = i+1
#     while j < len(arr):
#         width = j-i
#         height = min(arr[i],arr[j])
        
#         area = width*height
        
#         if area > ans :
#             ans = area  
#             container = (arr[i],arr[j])
        
#         j+=1
#     i+=1

# print(ans)
# print(container)    


#===========================================================================================================================================


i = 0
j = len(arr)-1
ans = 0
while i < j :
    width = j-i
    length = min(arr[i],arr[j])
    area  = length*width
    if area > ans :
        ans = area 
        containers = (f"Container is {arr[i],arr[j]}")
    
    if arr[i] < arr[j]:
        i+=1
    else :
        j-=1         

print(ans)
print(containers)
