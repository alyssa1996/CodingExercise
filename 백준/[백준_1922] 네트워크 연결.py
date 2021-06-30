def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

computers = int(input())
line = int(input())
edges = []
parent = [0]*(computers+1)

for i in range(1, computers+1):
    parent[i] = i

for _ in range(line):
    ca, cb, cost = map(int, input().split())
    edges.append((cost, ca, cb))

edges.sort()

result = 0
for edge in edges:
    cost, ca, cb = edge
    if find_parent(parent, ca) != find_parent(parent, cb):
        union_parent(parent, ca, cb)
        result += cost

print(result)
