import sys

def find_parent(parent, star):
    if parent[star] != star:
        parent[star] = find_parent(parent, parent[star])
    return parent[star]

def union_parent(parent, star1, star2):
    pstar1 = find_parent(parent, star1)
    pstar2 = find_parent(parent, star2)
    if pstar1 < pstar2:
        parent[pstar2] = pstar1
    else:
        parent[pstar1] = pstar2

input = sys.stdin.readline
n = int(input())
parent = [number for number in range(n+1)]
locations = dict()

for key in range(1, n+1):
    x, y = map(float, input().split())
    locations[(x, y)] = key

edges = []
cost = 0
loc = list(locations.keys())
for idx1 in range(len(loc)):
    for idx2 in range(idx1+1, len(loc)):
        x1, y1, x2, y2 = loc[idx1][0], loc[idx1][1], loc[idx2][0], loc[idx2][1]
        distance = ((x2-x1)**2 + (y2 - y1)**2)**0.5
        edges.append((distance, loc[idx1], loc[idx2]))

edges.sort()

for edge in edges:
    distance, star1, star2 = edge
    if find_parent(parent, locations[star1]) != find_parent(parent, locations[star2]):
        union_parent(parent, locations[star1], locations[star2])
        cost += distance

print(round(cost, 2))
        
