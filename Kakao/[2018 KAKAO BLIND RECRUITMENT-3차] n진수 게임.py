import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    numbers = []
    
    for num in range(t*m):
        current_num = convert(num, n)
        if len(current_num) > 1:
            numbers.extend(list(current_num))
        else:
            numbers.append(current_num)
    
    for idx in range(p-1, len(numbers), m):
        answer += numbers[idx]
    
    return answer[:t]
