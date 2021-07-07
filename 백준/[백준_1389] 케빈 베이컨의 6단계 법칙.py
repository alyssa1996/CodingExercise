import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = 1e9
relationship = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    relationship[i][i] = 0

for _ in range(m):
    i, j = map(int, input().split())
    relationship[i][j] = 1
    relationship[j][i] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            relationship[i][j] = min(relationship[i][j], relationship[i][k]+relationship[k][j])
            relationship[j][i] = relationship[i][j]


answer = (0, INF)
for number in range(1, n+1):
    current = sum(relationship[number][1:])
    if current < answer[1]:
        answer = (number, current)

print(answer[0])
        
