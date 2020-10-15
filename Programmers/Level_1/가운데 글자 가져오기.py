def solution(s):
    start=len(s)//2
    answer = s[start-1:start+1] if len(s)%2==0 else s[start]
    return answer
