import sys

n=int(input())
array=[]
for i in range(n):
    t,p=map(int,sys.stdin.readline().split())
    array.append((t,p))

def max_profit(index):
    t=index
    result=0
    while t<n:
        if t+array[t][0]>=n:
            break
        result+=array[t][1]
        t+=array[t][0]
    return result

result=0
for i in range(n):
    current=max_profit(i)
    if result<current:
        result=current

print(result)
