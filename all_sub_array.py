#Print all sub array
str = "rajat"
i=0
main_ans=[]
while(i<len(str)):
    ans=""
    j=i
    while(j<len(str)):
        ans=ans+str[j]
        j=j+1
        main_ans.append(ans)
        # print(ans)
    i=i+1       
    
    
    
print(main_ans)