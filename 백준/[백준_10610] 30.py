import sys

numbers = list(sys.stdin.readline().strip())
numbers.sort(reverse=True)

if numbers[-1] == '0' and sum(map(int, numbers))%3 == 0:
    print(''.join(numbers))
else:
    print(-1)
