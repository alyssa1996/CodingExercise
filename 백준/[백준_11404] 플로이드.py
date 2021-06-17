import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
bus = [[INF]*(n+1) for _ in range(n+1)]

for city in range(1, n+1):
    bus[city][city] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus[i][j] = min(bus[i][j], bus[i][k]+bus[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == INF:
            bus[i][j] = 0

for city in range(1, n+1):
    print(' '.join(map(str, bus[city][1:])))
