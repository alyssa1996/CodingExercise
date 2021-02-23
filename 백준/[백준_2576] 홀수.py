numbers=list()
for i in range(7):
    n=int(input())
    if n%2==1:
        numbers.append(n)

if len(numbers):
    print("%d \n%d"%(sum(numbers),min(numbers)))
else:
    print(-1)
