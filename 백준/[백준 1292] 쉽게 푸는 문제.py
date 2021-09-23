start, end = map(int, input().split())

numbers = []
number = 1
while len(numbers) <= end:
    numbers += [number]*number
    number += 1

print(sum(numbers[start-1:end]))
