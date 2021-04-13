def solution(n):
    answer = 0
    count=bin(n).count('1')
    while True:
        n+=1
        next_count=bin(n).count('1')
        if count==next_count:
            break
    return n
