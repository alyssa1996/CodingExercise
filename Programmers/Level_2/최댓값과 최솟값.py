def solution(s):
    answer = ''
    ex=list(map(int,s.split(" ")))
    answer=str(min(ex))+" "+str(max(ex))
    return answer
