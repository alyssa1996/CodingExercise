h,m=map(int,input().split())

changedMin=m-45
if changedMin>=0:
    print(h,changedMin)
else:
    changedMin+=60
    if h:
        print(h-1,changedMin)
    else:
        print(23,changedMin)
