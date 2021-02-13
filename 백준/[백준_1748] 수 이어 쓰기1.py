n=int(input())
number=len(str(n))
result=0
for i in range(number-1):
    result+=9*(10**i)*(i+1)
    
result+=number*(n-(10**(number-1))+1)
print(result)
