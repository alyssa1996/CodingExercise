def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a < parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

n, m = map(int, input().split())
parent = [number for number in range(n+1)]

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
        
