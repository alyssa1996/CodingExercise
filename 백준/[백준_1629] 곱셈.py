a, b, c = map(int, input().split())

def divide(a, b):
    if b == 1:
        return a % c

    temp = divide(a, b//2)
    if b % 2 == 0:
        return temp * temp % c
    return temp * temp * a % c

print(divide(a, b))
