n=int(input())
ar=[0]*(n+1)

for i in range(1,n+1):
    ar[i]=int(input())

print(ar)
for i in range(2,n+1):
    ar[i]=max(ar[i-1],ar[i-2]+ar[i])
    print(ar)

print(ar[n])
