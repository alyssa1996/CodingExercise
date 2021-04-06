n=int(input())
numbers=[]

for i in range(n):
    numbers.append(int(input()))

max_value=max(numbers)
result=[]
for i in range(2,max_value+1):
    first=numbers[0]%i
    check=True
    for j in range(1,len(numbers)):
        if numbers[j]%i==first:
            continue
        else:
            check=False
            break
    if check:
        result.append(i)

print(' '.join(map(str,result)))
