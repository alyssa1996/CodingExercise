def conversion(string):
    if len(string)==0:
        return string
    
    op,cl=0,0
    stack=[]
    index=0
    check=True
    for i in range(len(string)):
        if string[i]=="(":
            stack.append("(")
            op+=1
        else:
            if len(stack)==0:
                check=False
            else:
                stack.pop()
            cl+=1
        if op==cl:
            index=i
            break
    
    u=string[:index+1]
    v=string[index+1:]
    if check:
        return u+conversion(v)
    else:
        new="("+conversion(v)+")"
        for i in range(1,len(u)-1):
            if u[i]=="(":
                new=new+")"
            else:
                new=new+"("
        return new
        
def solution(p):        
    return conversion(p)
