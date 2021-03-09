import sys
n,m=map(int,input().split())
rice=list(map(int,sys.stdin.readline().split()))
rice.sort()

start,end=0,rice[-1]
result=0
while start<=end:
    mid=(start+end)//2
    total=0
    for i in rice:
        if i>mid:
            total+=i-mid
    if m<=total:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)
