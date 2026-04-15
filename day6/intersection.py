# Intersection of unsorted array
arr1 = [10, 20, 30, 40, 50]
arr2 = [20, 70, 30, 90]

ans = []
i = 0

while i < len(arr1):
    j = 0
    while j < len(arr2):
        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            break
        j += 1
    i += 1

print(ans)