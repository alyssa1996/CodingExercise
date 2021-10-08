import sys
input = sys.stdin.readline
n, x = map(int, input().split())
visits = list(map(int, input().split()))

start, end = 0, x-1
current_visit = sum(visits[start:end+1])
max_visit = current_visit
counts = 1

while end < n-1:
    current_visit -= visits[start]
    start, end = start + 1, end + 1
    current_visit += visits[end]
    if max_visit < current_visit:
        max_visit  = current_visit
        counts = 1
    elif max_visit == current_visit:
        counts += 1

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(counts)
    


