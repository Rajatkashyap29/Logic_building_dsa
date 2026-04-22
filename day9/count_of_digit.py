def countDigit(n):
    count = 0
    while n > 0 :
        count = count + 1
        
        q = n//10
        n=q
    return count

# n=int(input("PLEASE ENTER A NUMBER ->"))
# count = countDigit(n)
# print ("AFTER CALCULATION COUNT IS -:",count)