import sys
input = sys.stdin.readline

def is_added(s, number):
    return number in s

m = int(input())
s = set()
for _ in range(m):
    inputs = input().split()
    if inputs[0] == 'add':
        s.add(int(inputs[1]))
    if inputs[0] == 'check':
        if is_added(s, int(inputs[1])):
            print(1)
        else:
            print(0)
    if inputs[0] == 'remove':
        s.discard(int(inputs[1]))
    if inputs[0] == 'toggle':
        number = int(inputs[1])
        if is_added(s, number):
            s.remove(number)
        else:
            s.add(number)
    if inputs[0] == 'all':
        s = set([num for num in range(1, 21)])
    if inputs[0] == 'empty':
        s = set()
    
