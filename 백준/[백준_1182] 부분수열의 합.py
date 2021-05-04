from itertools import combinations

n, s = map(int,input().split())
numbers = list(map(int, input().split()))
count = 0
for value in range(1, n+1):
    combi = list(combinations(numbers, value))
    for candidate in combi:
        if sum(candidate) == s:
            count += 1

print(count)
