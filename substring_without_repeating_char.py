#Print all sub array
# str = "rajat"
str="abacab"

i=0
main_ans=[]
max_len =0
while(i<len(str)):
    ans=""
    j=i
    while(j<len(str)):
        if str[j] in ans:
            break
        else:
            ans=ans+str[j]
            if len(ans)>max_len:
                max_len = len(ans)
            j=j+1
            main_ans.append(ans)
        # print(ans)
    i=i+1       
    
    
    
print(max_len)