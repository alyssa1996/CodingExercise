import sys
from itertools import combinations
n=int(input())
coin=list(map(int,sys.stdin.readline().split()))

result=[]
for i in range(1,n+1):
    temp=list(combinations(coin,i))
    for j in range(len(temp)):
        result.append(sum(temp[j]))

result=sorted(set(result))
min_value=1
while True:
    if min_value in result:
        min_value+=1
        continue
    else:
        break

print(min_value)


#모범답안
coin.sort()
target=1
for x in coin:
    if target<x:
        break
    target+=x

print(target)
