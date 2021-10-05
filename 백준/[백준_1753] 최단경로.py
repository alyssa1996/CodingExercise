import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
path = [INF]*(v+1)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

queue = []
heapq.heappush(queue, ((0, start)))
path[start] = 0
while queue:
    prev_cost, prev_node = heapq.heappop(queue)
    if path[prev_node] < prev_cost:
        continue
    for next_node, next_cost in graph[prev_node]:
        cost = prev_cost + next_cost
        if cost < path[next_node]:
            path[next_node] = cost
            heapq.heappush(queue, (cost, next_node))

for idx in range(1, v+1):
    if path[idx] == INF:
        print('INF')
    else:
        print(path[idx])
