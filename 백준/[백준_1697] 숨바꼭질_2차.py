n, k = map(int, input().split())
import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
total_count = []
numbers = defaultdict(int)
numbers[n] = 1
def dfs(subin, sister, count):
    if subin == sister:
        total_count.append(count)
        return
    if subin in numbers and numbers[subin] < count:
        return
    for move in [-1, 1, 2]:
        if move == 2:
            numbers[subin*move] = count +1
            dfs(subin*move, sister, count+1)
            numbers[subin*move] -= 1
        else:
            numbers[subin+move] += count + 1
            dfs(subin+move, sister, count+1)
            numbers[subin+move] -= 1

dfs(n, k, 0)
print(total_count)
