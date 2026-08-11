# arr = [1, 1, 2, 2, 3, 3]
# tar = 4

# i = 0
# while i < len(arr):
#     ans = tar - arr[i]
#     j = i + 1

#     while j < len(arr):
#         if arr[j] == ans:
#             print(f"Pair is ({arr[i]}, {arr[j]})")
#             break
#         j += 1
#     current = arr[i]
#     while i < len(arr) and arr[i] == current:
#         i += 1
        


arr = [1, 1, 2, 2, 3, 3]
tar = 4

i = 0   
j = len(arr)-1

while i < j:
  ans = arr[i] + arr [j]
  
  if ans == tar :
    print(f"Pair is ({arr[i]}, {arr[j]})")
    
    copyofi = arr[i]
    copyofj = arr[j]
    
    while i < j and arr[i] == copyofi:
      i+=1
    while i < j and arr[j] == copyofj:  
      j-=1
  
  elif ans < tar:
    i+=1
  else:
    j-=1      
    
       
        
        