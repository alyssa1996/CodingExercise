import sys
input = sys.stdin.readline

DELTAS = [(0,1), (0, -1), (1, 0), (-1, 0)]
r, c = map(int, input().split())
board = []

for _ in range(r):
    board.append(input())

queue = set()
answer = 0
queue.add((0, 0, 1, board[0][0]))

while queue:
    cx, cy, cnt, alphabet = queue.pop()
    answer = max(answer, cnt)
    for x, y in DELTAS:
        nx, ny = cx+x, cy+y
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alphabet:
            queue.add((nx, ny, cnt+1, alphabet+board[nx][ny]))

print(answer)

