def get_gcd(a, b):
    if b == 0 :
        return a
    return get_gcd(b, a%b)

n = int(input())
rings = list(map(int, input().split()))

for idx in range(1, len(rings)):
    gcd = get_gcd(rings[0], rings[idx])
    print("%d/%d"%(rings[0]//gcd, rings[idx]//gcd))
