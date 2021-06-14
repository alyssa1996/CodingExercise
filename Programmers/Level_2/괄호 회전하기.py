from collections import deque
def check_bracket(s):
    stack = []
    couple = { '}':'{', ')':'(', ']':'['}
    for bracket in s:
        if bracket in ['(', '{', '[']:
            stack.append(bracket)
        elif stack and stack[-1] == couple[bracket]:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True

def solution(s):
    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        s.append(s.popleft())
        if check_bracket(s):
            answer += 1
    
    return answer
