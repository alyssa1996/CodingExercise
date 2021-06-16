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

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    parent = [number for number in range(n+1)]
    edges = []
    result = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    for edge in edges:
        a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1
    
    print(result)
