#Brute force
arr = [7, 10, 15, 12, 81, 9, 8]
required_sum = 20

i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if arr[i] + arr[j] == required_sum:
            print("(",arr[i],"And", arr[j],")","are required pair pair for required sum")
        j += 1
    i += 1




# Optimal solution usuing dict


arr = [7, 10, 15, 12, 81, 9, 8]
required_sum = 20

d = {}
i = 0

while i < len(arr):
    r_num = required_sum - arr[i]
    r = d.get(r_num, None)
    
    if r is None:
        d[arr[i]] = i
    else:
        print(arr[i], r_num)
        break
    
    i += 1