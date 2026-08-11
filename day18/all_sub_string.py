s = input("Enter a string: ")

i = 0
ans = []

while i < len(s):
    temp = ""
    j = i

    while j < len(s):
        temp += s[j]
        if temp not in ans :
         ans.append(temp)
        j += 1

    i += 1

print(ans)