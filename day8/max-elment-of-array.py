arr = [21, 3, 14, 7, 28, 11]
i = 0
max = 0

while i < len(arr):
    if arr[i] > max:
        max= arr[i]
    i += 1

print(max)