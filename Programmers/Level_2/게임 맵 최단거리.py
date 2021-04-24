from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def route_check(cx, cy, n, m, maps):
    check = True
    for idx in range(4):
        nx = dx[idx] + cx
        ny = dy[idx] + cy
        if 0 <= nx <= n and 0 <= ny <= m:
            if maps[nx][ny]:
                check = False
    return check

def solution(maps):
    n, m = len(maps) -1, len(maps[0]) - 1
    if route_check(n, m, n, m, maps):
        return -1
    
    road_map = [[-1]*(m+1) for _ in range(n+1)]
    road_map[0][0] = 1
    queue = deque([(0,0)])
    while queue:
        cx, cy = queue.popleft()
        for idx in range(4):
            nx = dx[idx] + cx
            ny = dy[idx] + cy
            if 0 <= nx <= n and 0 <= ny <= m:
                if maps[nx][ny] and road_map[nx][ny] == -1:
                    road_map[nx][ny] = road_map[cx][cy] + 1
                    queue.append((nx,ny))
    
    return road_map[-1][-1]
