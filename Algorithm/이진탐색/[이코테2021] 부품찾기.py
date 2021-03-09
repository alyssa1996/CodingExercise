import sys

def binary_search(start,end,target,stock):
    if end<start:
        return False
    mid=(start+end)//2
    if target==stock[mid]:
        return True
    elif target<stock[mid]:
        return binary_search(start,mid-1,target,stock)
    else:
        return binary_search(mid+1,end,target,stock)

n=int(input())
stock=list(map(int,sys.stdin.readline().split()))
m=int(input())
request=list(map(int,sys.stdin.readline().split()))

stock.sort()
for i in request:
    if binary_search(0,n-1,i,stock):
        print('yes',end=" ")
    else:
        print('no',end=" ")
