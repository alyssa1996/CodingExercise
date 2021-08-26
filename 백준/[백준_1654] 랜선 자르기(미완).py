import heapq, math
import sys
input = sys.stdin.readline

k, n = map(int, input().split())

heap = []
small = -1e9
for _ in range(k):
    string = -int(input())
    if small < string :
        small = string
    heapq.heappush(heap, string)

while len(heap) < n:
    long = heapq.heappop(heap)
    a, b = math.ceil(long/2), math.floor(long/2)
    print(small, a, b)
    if small < a:
        small = a
    else:
        a, b = small, long-small
        print(a,b)
    heapq.heappush(heap, a)
    heapq.heappush(heap, b)

print(heap)
print(small)
'''
last = heapq.heappop(heap)
if len(heap)+1 == n - 1:
    max_length = max(heap)
    if last-max_length < max_length:
        print(-max_length)
    else:
        print(-(last-max_length))
else:
    print(-last)
'''

