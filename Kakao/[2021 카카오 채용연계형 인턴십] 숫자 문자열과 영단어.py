def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, numbers in enumerate(numbers):
        s = s.replace(numbers, str(idx))
    return int(s)
