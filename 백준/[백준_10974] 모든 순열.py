from itertools import permutations
n = int(input())
numbers = [x for x in range(1,n+1)]
candidates = list(permutations(numbers, n))
candidates.sort()
for value in candidates:
    for idx in range(n):
        print(value[idx],end = ' ')
    print()
