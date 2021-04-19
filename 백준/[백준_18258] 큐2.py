from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
queue=deque()
for _ in range(n):
    msg = input().split()
    if msg[0] == 'push':
        queue.append(int(msg[1]))

    if msg[0] == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)

    if msg[0] == 'size':
        print(len(queue))

    if msg[0] == 'empty':
        if queue: print(0)
        else: print(1)

    if msg[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)

    if msg[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
