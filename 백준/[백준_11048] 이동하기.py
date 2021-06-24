import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            board[i][j] += board[i][j-1]
        elif j == 0:
            board[i][j] += board[i-1][j]
        else:
            board[i][j] += max(board[i-1][j], board[i][j-1], board[i-1][j-1])

print(board[n-1][m-1])
