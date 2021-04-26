import sys
input = sys.stdin.readline
dp={}

def w(a,b,c):
    if (a,b,c) in dp:
        return dp[(a,b,c)]

    if a <= 0 or b<= 0 or c <= 0:
        dp[(a,b,c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[(a,b,c)] = w(20,20,20)
    elif a < b < c:
        dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[(a,b,c)]

while True:
    a, b, c = map(int,input().split())
    if a == b == c == -1:
        break
    if not (a,b,c) in dp:
        w(a,b,c)
    print("w(%d, %d, %d) = %d"%(a,b,c,dp[(a,b,c)]))
    
