is_prime = [True]*10001
is_prime[0] = False
is_prime[1] = False
for num in range(10001):
    if not is_prime[num]:
        continue
    for multiple in range(num*num, 10001, num):
        is_prime[multiple] = False

prime_number = set()
for num in range(10001):
    if is_prime[num]:
        prime_number.add(num)

tc = int(input()) 
for _ in range(tc):
    n = int(input())
    candidate = []
    for num in range((n//2)+1):
        if num in prime_number and n-num in prime_number:
            difference = n-(num*2)
            candidate.append((num, n-num, difference))
    candidate.sort(key = lambda x : x[2])
    print(candidate[0][0], candidate[0][1])
