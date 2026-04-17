arr = [21, 3, 14, 7, 28, 11]
i = 0
min = 99999

while i < len(arr):
    if arr[i] < min:
        min= arr[i]
    i += 1

print(min)