arr = [2,4,6,8,10]
r_p =1
l_p =1

i=0
while(i<len(arr)):
    j=i+1
    r_p = r_p*arr[j]
    
    i+=1

i=0
while(i>len(arr)):
    j=i-1
    l_p = l_p*arr[j]
    
    i+=1

ans = l_p * r_p
print(ans)        

