from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

village = []
house = []
chicken = []
for i in range(n):
    village.append(list(map(int, input().split())))
    for j in range(n):
        if village[i][j] == 1:
            house.append((i, j))
        if village[i][j] == 2:
            chicken.append((i, j))

combi = list(combinations(chicken, m))

result = 1e9
for chickens in combi:
    candidate = 0
    for hi, hj in house:
        distance = 1e9
        for ci, cj in chickens:
            distance = min(distance, abs(ci-hi)+abs(cj-hj))
        candidate += distance
    result = min(candidate, result)

print(result)
        

