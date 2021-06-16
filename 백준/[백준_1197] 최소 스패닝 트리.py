import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

v, e = map(int, input().split())
parent = [number for number in range(v+1)]
edges = []
result = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort() 

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)
