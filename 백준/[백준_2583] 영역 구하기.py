import sys
from collections import deque
input = sys.stdin.readline
m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]

def sperated_part(x, y):
    candidates = deque([(x, y)])
    board[x][y] = 1
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    size = 0
    while candidates:
        cx, cy = candidates.popleft()
        size += 1
        for dx, dy in DIRECTIONS:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
                candidates.append((nx, ny))
                board[nx][ny] = 1
                
    return size


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] = 1

count = 0
parts = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            count += 1
            parts.append(sperated_part(i, j))

parts.sort()
print(count)
print(' '.join(map(str, parts)))
