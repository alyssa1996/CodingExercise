def move(n, energy):
    if n == 0:
        return energy
    if n % 2 == 0:
        return move(n//2, energy)
    return move(n-1, energy+1)

def solution(n):
    return move(n, 0)
