n = int(input("Please enter a number: "))

x = 0
y = 1
i = 0

print("\nFibonacci Series:")

while i < n:
    print(x, end=" ")
    
    new = x + y
    x = y
    y = new
    
    i += 1