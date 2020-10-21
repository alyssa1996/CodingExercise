#프로그래머스

def solution(n, lost, reserve):
    same=list(set(lost)&set(reserve))
    for i in same:
        lost.remove(i)
        reserve.remove(i)
    lost=sorted(lost)
    reserve=sorted(reserve)
    
    for i in reserve:
        if i in lost:
            lost.remove(i)
        elif i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer=n-len(lost)
    return answer
