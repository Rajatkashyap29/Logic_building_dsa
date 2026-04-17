s="ABDEIMXLP"
vowel=[]
cons=[]
i=0
while(i<len(s)):
    if s[i] in ('a','A','e','E','i','I','o','O','u','U'):
        vowel.append(s[i])
    else:
        cons.append(s[i])
    
    i+=1     

print(vowel)   
print(cons)    