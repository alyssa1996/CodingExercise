import sys
input = sys.stdin.readline

n = int(input())
numbers = [0]*10_001
for _ in range(n):
    number = int(input())
    numbers[number] += 1

for number, counted in enumerate(numbers):
    for count in range(counted):
        print(number)
