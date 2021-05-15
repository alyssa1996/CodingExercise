import math
def solution(n,a,b):
    answer = 1

    if b < a:
        a, b = b, a
    while True:
        if b%2 == 0 and abs(b-a) == 1:
            break
        a, b = math.ceil(a/2), math.ceil(b/2)
        answer += 1
        
    return answer
