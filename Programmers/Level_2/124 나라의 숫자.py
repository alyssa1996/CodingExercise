def conversion(n):
    if n<=3:
        if n==1 or n==2:
            return str(n)
        else:
            return '4'
    
    if n%3==0:
        return conversion(n//3-1)+'4'
    elif n%3==1:
        return conversion(n//3)+'1'
    elif n%3==2:
        return conversion(n//3)+'2'

def solution(n):
    return conversion(n)
