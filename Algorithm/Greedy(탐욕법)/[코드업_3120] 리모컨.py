def upTemp(current,goal):
    result=0
    while current!=goal:
        if current+10>goal:
            if current+5>goal:
                current+=1
            else:
                current+=5
        else:
            current+=10
        result+=1
    return result

def downTemp(current,goal):
    result=0
    while current!=goal:
        print(current)
        if current-10<goal:
            if current-5<goal:
                current-=1
            else:
                current-=5
        else:
            current-=10
        result+=1
    return result


a,b=input("").split(" ")
a,b=int(a),int(b)

if a<b:
    print(upTemp(a,b))
else:
    print(downTemp(a,b))
