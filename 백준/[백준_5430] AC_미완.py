import sys
from collections import deque

def run_oper(operation,numbers):
    check=True
    pop_direction=1
    for i in range(len(operation)):
        if operation[i]=='R':
            pop_direction*=(-1)
            
        if operation[i]=='D':
            if len(numbers)==0:
                check=False
                break
            
            if pop_direction==-1:
                numbers.pop()
            elif pop_direction==1:
                numbers.popleft()
                
    if pop_direction==-1:
        numbers.reverse()
        
    if check:
        return str(list(numbers)).replace(' ','')
    else:
        return 'error'

input=sys.stdin.readline
for i in range(int(input())):
    operation=list(input())
    length=int(input())
    temp=input()[1:-2].split(',')
    numbers=deque(list(map(int,temp)))
            
    print(run_oper(operation,numbers))
    
    
    
