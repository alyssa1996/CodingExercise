n = int(input())
board = [[0]*(n+1)]*(n+1)

def is_able(i, j, queen):
    for x, y in queen:
        if x == i or y == j or x+y == i+j or x-y == i-j:
            return False
    return True
    
def check_queen(x, y, queen):
    global case_count
    if len(queen) == n:
        case_count += 1
        return 
    for i in range(x, n+1):
        for j in range(y, n+1):
            if is_able(i, j, queen):
                queen.append((i,j))
                check_queen(i,j,queen)
                queen.pop()
        y = 1


case_count = 0
for y in range(1, n+1):
    queen = [(1, y)]
    check_queen(1, y, queen)
        
print(case_count)
