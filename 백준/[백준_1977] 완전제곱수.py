import math

m=int(input())
n=int(input())

minimum=math.ceil(m**(1/2))
value=minimum
total=0
while value**2<=n:
    total+=value**2
    value+=1
    
if total:
    print(total)
    print(minimum**2)
else:
    print(-1)
