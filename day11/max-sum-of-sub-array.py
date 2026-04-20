arr= [7,-2,-9,10,20,30,-6,-1,25]
i=0
ans=0
while i< len(arr):
    sum = arr[i]
    j=i+1
    while j < len(arr):
        sum = sum + arr[j]
        if sum > ans :
            ans = sum 
    
        j+=1        
    i+=1

print(ans)    



#---------------------------OPTIMAL VERSION -------------------------------
arr= [7,-2,-9,10,20,30,-6,-1,25]
i=0
current_sum = 0
ans = 0
while i<len(arr):
    current_sum = max(arr[i],current_sum+arr[i])
    ans = max(current_sum,ans)
    
    i+=1

print (ans)    
