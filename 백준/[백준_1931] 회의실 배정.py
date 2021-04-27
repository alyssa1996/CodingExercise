import sys
input = sys.stdin.readline
n = int(input())
time = []

for _ in range(n):
    a, b = map(int,input().split())
    time.append([a, b])
        
time.sort(key= lambda x:(x[1],x[0]))
result, end = 0, 0
for s,e in time:
    if s >= end:
        result += 1
        end = e
print(result)
