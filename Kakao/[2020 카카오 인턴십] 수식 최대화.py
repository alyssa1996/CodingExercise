from itertools import permutations

def calculation(x,y,oper):
    if oper == '+':
        return x+y
    if oper == '-':
        return x-y
    if oper == '*':
        return x*y

def operation(operator,exp):
    for op in operator:
        idx = 0
        while idx < len(exp):
            if exp[idx] == op:
                exp[idx-1] = calculation(exp[idx-1],exp[idx+1],exp[idx])
                exp.pop(idx+1)
                exp.pop(idx)
            else:
                idx += 1
    return abs(exp[0])

def solution(expression):
    result = 0
    operators = list(permutations(['+','-','*'],3))
    exp = []
    previous = 0
    
    for idx, value in enumerate(expression):
        if not value.isnumeric():
            exp.append(int(expression[previous:idx]))
            exp.append(value)
            previous = idx+1
    exp.append(int(expression[previous:]))
    
    for oper in operators:
        current = operation(oper,exp[:])
        if result < current:
            result = current
            
    return result
