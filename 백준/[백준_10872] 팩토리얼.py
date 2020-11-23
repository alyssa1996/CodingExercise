num=int(input())

if num<=1:
    print(1)
else:
    fact=1
    for i in range(2,num+1):
        fact*=i
    print(fact)
