import sys
input = sys.stdin.readline
n, m = map(int, input().split())
never_heard = set()
never_seen = set()
for _ in range(n):
    never_heard.add(input())

for _ in range(m):
    never_seen.add(input())

candidate = sorted(list(never_heard&never_seen))

print(len(candidate))
print(''.join(candidate))
