exp=input("").split(" ")
stack=list()
for i in exp:
    if i.isnumeric():
        stack.append(int(i))
    elif i in ['*','+','-']:
        end=stack.pop()
        start=stack.pop()
        if i=='*':
            stack.append(start*end)
        if i=="+":
            stack.append(start+end)
        if i=="-":
            stack.append(start-end)

print(stack[0])
