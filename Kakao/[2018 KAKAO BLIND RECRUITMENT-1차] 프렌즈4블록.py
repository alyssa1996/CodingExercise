from collections import deque

def check_board(blocks, board, m, n):
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                blocks.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)]) 
    return blocks

def rearrage_board(blocks, board, m, n):
    while blocks:
        x, y = blocks.popleft()
        if x == 0:
            board[x][y] = 0
        else:
            board[x][y], board[x-1][y] = board[x-1][y], 0
    
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if board[k][j] != 0:
                        break
                board[k][j], board[i][j] = 0, board[k][j]

    return board

def solution(m, n, board):
    for idx in range(m):
        board[idx] = list(board[idx])

    answer = 0
    while True:
        blocks = check_board(set(), board, m, n)
        if len(blocks) == 0:
            break
        answer += len(blocks)
        blocks = deque(sorted(list(blocks)))
        board = rearrage_board(blocks, board, m, n)

    return answer
