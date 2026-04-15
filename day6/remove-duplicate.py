# arr = [10,20,30,10,17,32,20,43,34,32,20]
# ans = []
# i = 0

# while i < len(arr):
#     if arr[i] not in ans:
#         ans.append(arr[i])
#     i += 1

# print(ans)      
        
#-------------better apporach ------------------------------

# arr = [10,20,30,10,17,32,20,43,34,32,20]
# ans = list(set(arr))
# print(ans)   
        
        
arr = [10,20,30,10,17,32,20,43,34,32,20]        
ans= set()
i=0
while i < len(arr):
    ans.add(arr[i])
    i += 1

print(ans)
