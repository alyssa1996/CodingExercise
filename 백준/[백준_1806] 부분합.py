import sys
input = sys.stdin.readline
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
sum_all = 0
min_length = 100_000
length = 0

while end <= n:
    if sum_all <= s :
        if end == n:
            break
        sum_all += numbers[end]
        end += 1
        length += 1
    else:
        sum_all -= numbers[start]
        start += 1
        length -= 1
    if s <= sum_all and length < min_length:
        min_length = length
        if length == 1:
            break
        
if min_length == 100_000:
    print(0)
else:
    print(min_length)
