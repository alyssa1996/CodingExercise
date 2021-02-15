a,b,c=map(int,input().split())
if c-b:
    result=a//(c-b)
    if result<0:
        print(-1)
    else:
        print(result+1)
else:
    print(-1)

