import sys
input = sys.stdin.readline
N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse = True)
max_weight = 0
for idx in range(N):
    current_max_weight = rope[idx]*(idx+1)
    if max_weight < current_max_weight:
        max_weight = current_max_weight

print(max_weight)
