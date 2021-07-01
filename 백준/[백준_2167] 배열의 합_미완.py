import sys
input = sys.stdin.readline
n, m = map(int, input().split())
boards = []

for _ in range(n):
    boards.append(list(map(int, input().split())))

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = 0
    for cx in range(i-1, x):
        result += sum(boards[cx][j-1:y])
    print(result)
