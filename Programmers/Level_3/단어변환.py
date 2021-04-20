def check_differ(str1,str2):
    count=0
    for idx in range(len(str1)):
        if str1[idx] == str2[idx]:
            continue
        count+=1
    return count

from collections import deque
def solution(begin, target, words):
    if not target in words:
        return 0
    
    answer = 0
    check=[False for i in range(len(words))]
    success=False
    dq=deque()
    dq.append(begin)
    while dq:
        answer+=1
        loop=len(dq)
        for _ in range(loop):
            current=dq.popleft()
            for idx,value in enumerate(words):
                dif=check_differ(current,value)
                if not check[idx] and dif == 1:
                    check[idx]=True
                    dq.append(value)
                    if value == target:
                        return answer
