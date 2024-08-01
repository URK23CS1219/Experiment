s = input("enter the infix expression:")

stack = []
output = ""

for i in range(len(s) - 1, -1, -1):
    if s[i].isalpha():
        output += s[i]
    elif s[i] == '+' or s[i] == '-':
        while stack and stack[-1] != ')':
            output += stack.pop()
        stack.append(s[i])
    elif s[i] == '*' or s[i] == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '^'):
            output += stack.pop()
        stack.append(s[i])
    elif s[i] == '^':
        while stack and stack[-1] == '^':
            output += stack.pop()
        stack.append(s[i])
    elif s[i] == '(':
        while stack and stack[-1] != ')':
            output += stack.pop()
        stack.pop()
    elif s[i] == ')':
        stack.append(s[i])

while stack:
    output += stack.pop()

print(output[::-1])
