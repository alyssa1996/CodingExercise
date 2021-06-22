from itertools import combinations
import sys
input = sys.stdin.readline
n, k  = map(int, input().split())
vw = [0]*(k+1)
items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
    vw[w] = v

items.sort()

for case in range(2, n):
    candidates = list(combinations(items, case))
    for candidate in candidates:
        weights = sum([w for w, v in candidate])
        if weights <= k:
            values = sum([v for w, v in candidate])
            vw[weights] = max(vw[weights], values)

print(max(vw))
            
            
        
