n=int(input())

first,second,result=1,2,0
for i in range(2,n):
    result=(first+second)%10007
    first,second=second,result

if n==1:
    print(first)
elif n==2:
    print(second)
else:
    print(result)
