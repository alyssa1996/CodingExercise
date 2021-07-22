from itertools import permutations
n = int(input())
nums = tuple(map(int, input().split()))
combis = list(permutations(list(nums), len(nums)))
combis.sort()

if nums == combis[-1]:
    print(-1)
else:
    idx = combis.index(nums)
    print(' '.join(map(str, combis[idx+1])))
