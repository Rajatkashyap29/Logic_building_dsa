#check Palindrome

str = "NAMAN"
i=0
j=len(str)-1
Flag=True

while(i<len(str)/2):
    if str[i] != str[j]:
        Flag = False
        break
    i+=1
    j-=1
    
if Flag == True :
    print("yes it is a valid palindrome")  

else:
    print("no it is not valid palindrome")      
    