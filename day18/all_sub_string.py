s = input("Enter a string: ")

i = 0
while i < len(s):
    temp = ""   # reset for each i
    j = i
    
    while j < len(s):
        temp = temp + s[j]
        print(temp)
        j += 1
        
    i += 1