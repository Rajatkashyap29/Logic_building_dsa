arr = [6, 8, 0, 1, 3]

stack = []
ans = []

i = len(arr) - 1

while i >= 0:

    while len(stack) > 0 and stack[-1] <= arr[i]:
        stack.pop()

    if len(stack) == 0:
        ans.append(-1)
    else:
        ans.append(stack[-1])

    stack.append(arr[i])
    i -= 1

ans.reverse()

print(ans)