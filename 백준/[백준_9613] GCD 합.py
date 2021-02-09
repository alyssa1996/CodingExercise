from sys import stdin
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

testcase=int(stdin.readline().strip())
for i in range(testcase):
    numbers=list(map(int,stdin.readline().split()))
    total=0
    for j in range(1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if numbers[j]>numbers[k]:
                total+=gcd(numbers[j],numbers[k])
            else:
                total+=gcd(numbers[k],numbers[j])
    print(total)
