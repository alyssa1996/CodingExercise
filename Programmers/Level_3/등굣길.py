def solution(m, n, puddles):
    roads = [[0]*m for _ in range(n)]
    DELTAS = [(0, -1), (-1, 0)]
    NUMBER = 1_000_000_007
    
    for y, x in puddles:
        roads[x-1][y-1] = -1
    
    roads[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if roads[i][j] == -1:
                continue
            for x, y in DELTAS:
                cx, cy = i+x, j+y
                if 0 <= cx < n and 0 <= cy < m and roads[cx][cy] != -1:
                    roads[i][j] += roads[cx][cy]
            roads[i][j] = (roads[i][j]%NUMBER)

    return roads[n-1][m-1]
