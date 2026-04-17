# check ANAGRAM
str1="RAMA"
str2="MAAR"

d1={}
i=0
while(i<len(str1)):
    old_value = d1.get(str1[i],0)
    d1[str1[i]] = old_value+1
    i+=1

d2={}
j=0
while(j<len(str2)):
    old_value = d2.get(str2[j],0)
    d2[str2[j]] = old_value+1
    j+=1
    

print(d1)
print(d2)

if d1 == d2 :
    print("yess")
else:
    print("noo")    


# ------------------------Optimized  Version -------------------
s1="RAJAT"
s2="RAZAT"

d={}
i=0
while(i<len(s1)):
    old_value=d.get(s1[i],0)
    d[s1[i]] = old_value+1
    i+=1

j=0
while(j<len(s2)):
    old_value=d.get(s2[j],0)
    d[s2[j]] = old_value-1
    j+=1

flag=True
for key , value in d.items():
    if value!=0:
        flag=False
        break
    
if flag == True:
    print("yes it is anagram") 
else:
    print("No it is not anagram ")             