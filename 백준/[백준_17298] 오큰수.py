import sys
n=int(input())
ar=list(map(int,sys.stdin.readline().split()))
stack=[]
result=[-1]

for i in range(n-1):
    stack.append(ar.pop())
    while True:
        if len(stack)==0:
            result.append(-1)
            break
        if ar[-1]<stack[-1]:
            result.append(stack[-1])
            break
        else:
            stack.pop()

result.reverse()
print(' '.join(map(str,result)))
