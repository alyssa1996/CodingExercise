def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a,b=map(int,input().split())
gcd=gcd(a,b)
print(gcd)
print(gcd*(a//gcd)*(b//gcd))
