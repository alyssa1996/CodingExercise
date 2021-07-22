import sys
input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    depth = list(map(int, input().split()))
    graph.append(depth)

for k in range(n):
    for i in range(n):
        for j in range(i, n):
            if graph[i][k]+graph[k][j] == 2:
                graph[i][j] = 1

for depth in range(n):
    print(' '.join(map(str, graph[depth])))
