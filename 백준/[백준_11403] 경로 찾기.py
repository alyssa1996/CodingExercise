import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
edges = [[] for _ in range(n)]
result = [[0]*n for _ in range(n)]

def get_route(root, edge):
    current_nodes = edge.copy()
    while current_nodes:
        node = current_nodes.pop()
        result[root][node] = 1
        if node == root:
            return
        get_route(root, edges[node])
    
for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            edges[i].append(j)

for node, edge in enumerate(edges):
    get_route(node, edge)

for idx in range(n):
    print(' '.join(map(str, result[idx])))
