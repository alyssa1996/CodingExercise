while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if a>b and a>c:
        c,a=a,c
    elif b>a and b>c:
        c,b=b,c
    if a**2+b**2==c**2:
        print('right')
    else:
        print('wrong')
