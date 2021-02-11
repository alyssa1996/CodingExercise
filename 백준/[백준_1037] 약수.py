from sys import stdin

n=int(stdin.readline())
numbers=list(map(int, stdin.readline().split()))
numbers.sort()
if len(numbers)==1:
    print(numbers[0]*numbers[0])
else:
    print(numbers[0]*numbers[len(numbers)-1])
