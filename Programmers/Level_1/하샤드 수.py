def solution(x):
    numbers=sum([int(i) for i in str(x)])
    if x%numbers==0:
        return True
    return False
