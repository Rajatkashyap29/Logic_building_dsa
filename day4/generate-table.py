n = int(input("Enter a number to generate TABLE : "))
i = 1
res = []
while i <= 10:
    ans = n * i
    t = str(n) + " * " + str(i) + " = " + str(ans)
    res.append(t)
    i += 1

for line in res:
    print(line)