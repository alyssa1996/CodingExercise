def solution(s):
    index=0
    answer=list()
    for i in s:
        if i==" ":
            answer.append(" ")
            index=0
            continue
        if index%2==0:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
        index+=1
    return ''.join(answer)
