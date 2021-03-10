import sys

def binary_search(start,end,array):
    if end<start:
        return False
    mid=(start+end)//2
    if array[mid]==mid:
        return mid
    elif array[mid]<mid:
        return binary_search(mid+1,end,array)
    else:
        return binary_search(start,mid-1,array)

n=int(input())
array=list(map(int,sys.stdin.readline().split()))
result=binary_search(0,n-1,array)
if result:
    print(result)
else:
    print(-1)
