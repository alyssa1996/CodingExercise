number=list(map(int,input()))

if len(number)==1:
    print(number[0])
else:
    result=0
    if 0 in number[:2] or 1 in number[:2]:
        result=number[0]+number[1]
    else:
        result=number[0]*number[1]
    for i in range(2,len(number)):
        if number[i]<=1:
            result+=number[i]
        else:
            result*=number[i]
    print(result)
    
    
