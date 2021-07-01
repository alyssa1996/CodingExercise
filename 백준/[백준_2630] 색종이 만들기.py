import sys
input = sys.stdin.readline
n = int(input())
board = []
colors = [0, 0]

def check_color(x, y, size):
    first_color = board[x][y]
    if size == 1:
        colors[first_color] += 1
        return
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if first_color != board[i][j]:
                size //= 2
                check_color(x, y, size)
                check_color(x+size, y, size)
                check_color(x, y+size, size)
                check_color(x+size, y+size, size)
                return

    colors[first_color] += 1
    return

for _ in range(n):
    board.append(list(map(int, input().split())))

check_color(0, 0, n)
print(colors[0])
print(colors[1])
