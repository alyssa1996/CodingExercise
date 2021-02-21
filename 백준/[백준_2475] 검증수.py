number=list(map(int,input().split()))
result=0
for i in number:
    result+=i**2
print(result%10)
