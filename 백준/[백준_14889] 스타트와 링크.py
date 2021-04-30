import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
n = int(input())
abilities = []
for _ in range(n):
    abilities.append(list(map(int,input().split())))

def get_total_power(members):
    total_power = 0
    for i in range(len(members)):
        for j in range(i, len(members)):
            mem1, mem2 = members[i] - 1, members[j] - 1
            total_power += abilities[mem1][mem2] + abilities[mem2][mem1]
    return total_power

combi = deque(list(combinations(set([x for x in range(1, n+1)]), n//2)))
result = 1e9
while combi:
    start_team = combi.popleft()
    link_team = combi.pop()
    power_difference = abs(get_total_power(start_team) - get_total_power(link_team))
    if power_difference < result:
        result = power_difference

print(result)

