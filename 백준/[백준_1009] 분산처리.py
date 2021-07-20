import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    a, b = map(int, input().split())
    last_numbers = []
    square_number = 1
    while True:
        current_number = str(a**square_number)[-1]
        if last_numbers and current_number == last_numbers[0]:
            break
        last_numbers.append(current_number)
    idx = b % len(last_numbers)
    if last_numbers[idx-1] == '0':
        print(10)
    else:
        print(last_numbers[idx-1])
    '''
    target = a**b
    target_str = str(target)
    if target_str[-1] == '0':
        print(10)
    else:
        print(target_str[-1])
    '''
