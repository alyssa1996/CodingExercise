import sys

def change_color(current_color):
    if current_color=='W':
        return 'B'
    if current_color=='B':
        return 'W'

def paint(chess_board,start):
    change=0
    for i in range(8):
        for j in range(8):
            if i==0 and j==0:
                if chess_board[i][j]!=start:
                    chess_board[i][j]=change_color(chess_board[i][j])
                    change+=1
            elif i>0 and j==0:
                if chess_board[i-1][j]==chess_board[i][j]:
                    chess_board[i][j]=change_color(chess_board[i][j])
                    change+=1
            else:
                if chess_board[i][j-1]==chess_board[i][j]:
                    chess_board[i][j]=change_color(chess_board[i][j])
                    change+=1
    return change

n,m=map(int,input().split())
board=[]

for i in range(n):
    board.append(list(sys.stdin.readline())[:-1])


row,column=0,0
result=64
while row+8<=n and column+8<=m:
    chess_board_white=[]
    chess_board_black=[]
    for i in range(row,row+8):
        chess_board_white.append(board[i][column:column+8])
        chess_board_black.append(board[i][column:column+8])

    start_white=paint(chess_board_white,'W')
    start_black=paint(chess_board_black,'B')

    if start_white<result:
        result=start_white
    if start_black<result:
        result=start_black

    if row+8<n and column+8==m:
        row+=1
        column=0
    else:
        column+=1
        
print(result)
    
    
