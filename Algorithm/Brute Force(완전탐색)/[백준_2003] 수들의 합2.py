n,m=input().split()
n,m=int(n),int(m)
numbers=list(map(int,input().split()))

i=1
count=0
check=[numbers[0]]

while i<=n:
    if sum(check)==m:
        count+=1
        check.pop(0)
    elif sum(check)<m:
        if i==n:
            break
        check.append(numbers[i])
        i+=1
    else:
        check.pop(0)

print(count)
