def solution(s):
    answer=''
    if s[0].isalpha():
        answer+=s[0].upper()
    else:
        answer+=s[0]
    for i in range(1,len(s)):
        if s[i].isalpha() and s[i-1]==' ':
            answer+=s[i].upper()
        elif s[i].isalpha() and s[i-1]!=' ':
            answer+=s[i].lower()
        else:
            answer+=s[i]
    
    return answer
