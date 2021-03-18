import sys
n=int(input())
array=list(map(int,sys.stdin.readline().split()))
array.reverse()
d=[1]*(n+1)

for i in range(1,n):
    for j in range(i):
        if array[j]<array[i]:
            d[i]=max(d[i],d[j]+1)

print(n-max(d))

