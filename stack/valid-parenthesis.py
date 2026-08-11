s = input("Enter parentheses: ")

stack = []
i = 0

while i < len(s):
    bracket = s[i]

    if bracket == '(' or bracket == '{' or bracket == '[':
        stack.append(bracket)
    else:
        if len(stack) == 0:
            print("Invalid")
            break

        top = stack.pop()

        if not ((bracket == ')' and top == '(') or
                (bracket == '}' and top == '{') or
                (bracket == ']' and top == '[')):
            print("Invalid")
            break

    i += 1
else:
    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")