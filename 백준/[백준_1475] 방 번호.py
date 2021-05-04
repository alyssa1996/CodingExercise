import math
n = input()
numbers = [0]*10
for num in n:
    if int(num) == 9:
        numbers[6] += 1
    else:
        numbers[int(num)] += 1

numbers[6] = math.ceil(numbers[6]/2)
print(max(numbers))
