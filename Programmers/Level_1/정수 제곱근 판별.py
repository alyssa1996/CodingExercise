def solution(n):
    if (n**0.5)==round(n**0.5):
        answer=((n**0.5)+1)**2
    else:
        answer=-1
    return answer
