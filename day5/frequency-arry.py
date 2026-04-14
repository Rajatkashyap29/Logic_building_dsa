#Basic 

# arr=[10,12,13,10,10,13,15]
# i=0
# while(i<len(arr)):
#     j=0 #todo
#     count=0
#     while(j<len(arr)):
#         if arr[i] == arr[j]:
#             count = count+1
#         j+=1  
#     print("count of",arr[i],"=",count)  
    
    
#     i+=1  


# print_kara_diya=[]

# arr=[10,12,13,10,10,13,15]
# i=0
# while(i<len(arr)):
#     j=0 #todo
#     count=0
#     while(j<len(arr)):
#         if arr[i] == arr[j]:
#             count = count+1
#         j+=1  
#     if arr[i] not in print_kara_diya:
#         print("count of",arr[i],"=",count)  
#         print_kara_diya.append(arr[i])
    
#     i+=1    
#------------BETTER APPORACH ------------

arr=[10,12,13,10,10,13,15]
d={}
i=0
while(i<len(arr)):
    old_value = d.get(arr[i],0)
    d[arr[i]] = old_value+1
    i+=1
    
for key,value in d.items():
    print("count of ",key, " is ",value)