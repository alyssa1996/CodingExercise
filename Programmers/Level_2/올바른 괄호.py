def solution(s):
    answer = True
    stack=list()
    for i in s:
        if i==")":
            if len(stack)==0 or stack[-1]==i:
                answer=False
                break
            elif stack[-1]=="(":
                stack.pop()
        else:
            stack.append('(')
    
    if len(stack)!=0:
        answer=False
    return answer
