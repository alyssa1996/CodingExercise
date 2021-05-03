m, n = map(int, input().split())
is_prime = [True]*(n+1)
is_prime[1] = False

for candidate in range(2,n+1):
    if not is_prime[candidate]:
        continue
    for multiple in range(candidate*candidate, n+1, candidate):
        is_prime[multiple] = False

for number in range(m, n+1):
    if is_prime[number]:
        print(number)
