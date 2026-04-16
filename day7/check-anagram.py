# check ANAGRAM
str1="RAMA"
str2="MAARs"

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