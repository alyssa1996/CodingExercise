n=int(input())
m=n//5
count=0
for i in range(1,m+1):
    if (n-(5*i))%3==0:
        count=i

if count:
    count+=(n-(5*count))//3
else:
    if n%3==0:
        count=n//3
    else:
        count=-1

print(count)
