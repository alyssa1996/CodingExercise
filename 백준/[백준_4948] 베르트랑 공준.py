import sys
input =  sys.stdin.readline
prime_numbers = set()

for number in range(2,(2*123456)+1):
    check = True
    for target in range(2,int(number**(1/2))+1):
        if number % target == 0:
            check = False
            break
    if check:
        prime_numbers.add(number)

def count_decimal(n):
    count = 0
    for num in range(n+1,(2*n)+1):
        if num in prime_numbers:
            count += 1
    return count

while True:
    n = int(input())
    if not n:
        break
    print(count_decimal(n))
