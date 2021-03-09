import sys
from bisect import bisect_left,bisect_right

n,x=map(int,input().split())
array=list(map(int,sys.stdin.readline().split()))

counted=bisect_right(array,x)-bisect_left(array,x)
if counted:
    print(counted)
else:
    print(-1)

'''시간복잡도가 O(logN)이어야 하는 문제의 조건에 부합하지 않음
counted=[0]*(array[-1]+1)

for i in range(len(array)):
    counted[array[i]]+=1

print(counted[x])
'''
