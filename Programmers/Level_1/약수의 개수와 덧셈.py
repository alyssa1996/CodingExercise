def count_divisor(number):
    count = 0
    for candidate in range(1, number+1):
        if number % candidate == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        if count_divisor(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer
