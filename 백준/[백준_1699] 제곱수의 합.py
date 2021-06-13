import math
number = int(input())
count = 0
while number:
    print(number)
    number -= (math.trunc(number**(1/2)))**2
    count += 1

print(count)
