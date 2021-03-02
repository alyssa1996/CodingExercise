s=input()

strings=[]
numbers=0
for i in s:
    if i.isdigit():
        numbers+=int(i)
    else:
        strings.append(i)

if numbers:
    print(''.join(sorted(strings))+str(numbers))
else:
    print(''.join(sorted(strings)))
