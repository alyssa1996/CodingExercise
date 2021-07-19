import sys
input = sys.stdin.readline
n = int(input())

numbers = {}
for _ in range(n):
    num = int(input())
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1

max_count = (0, 0)
for num, count in numbers.items():
    if (max_count[1] < count) or (max_count[1] == count and num < max_count[0]):
        max_count = (num, count)

print(max_count[0])
