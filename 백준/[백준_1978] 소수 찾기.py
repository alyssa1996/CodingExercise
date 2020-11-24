num=int(input())
numbers=[int(i) for i in input().split()]

count=0
for i in numbers:
    prime=2
    if i<prime:
        continue
    isPrime=True
    while prime<=int(i**0.5):
        if i%prime==0:
            isPrime=False
            break
        else:
            prime+=1
    if isPrime:
        count+=1

print(count)
