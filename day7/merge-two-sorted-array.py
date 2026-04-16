# merge two sorted array 

a1=[10,15,17,25,35,55,65]
a2=[11,12,19,20]

ans=[]
i=0
j=0
while(i<len(a1) and j<len(a2)):
    if a1[i]<a2[j]:
        ans.append(a1[i])
        i+=1
    else:
        ans.append(a2[j])
        j+=1



while(i<len(a1)):
    ans.append(a1[i])
    i+=1
    
while(j<len(a2)):
    ans.append(a2[j])
    j+=1


print(ans)        
                