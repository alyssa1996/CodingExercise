import sys
input = sys.stdin.readline
h, w, x, y = map(int, input().split())
a = [[0]*w for _ in range(h)]
b = []
for _ in range(h+x):
    b.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        if x <= i and y <= j:
            a[i][j] = b[i][j]-a[i-x][j-y]
        else:
            a[i][j] = b[i][j]
'''
for i in range(x, h-x+1):
    for j in range(y, w-y+1):
        print(b[i][j], a[i-x][j-y])
        a[i][j] = b[i][j]-a[i-x][j-y]

for i in range(h, h+x):
    for j in range(w):
        a[i-x][j] = b[i][j+y]
'''
for i in range(h):
    print(' '.join(map(str, a[i])))

