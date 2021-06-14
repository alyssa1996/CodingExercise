def solution(n):
    MAGIC_NUM = 1_000_000_007
    a, b = 1, 1
    for idx in range(n):
        a, b = (a+b)%MAGIC_NUM, a
    return b
