def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if b>a:
        a,b=b,a
    temp=gcd(b,a)
    print(temp*(b//temp)*(a//temp))

