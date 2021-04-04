def solution(s):
    answer = 1001
    if len(s)==1:
        answer=1
    
    for i in range(1,int(len(s)/2)+1):
        strings=[]
        index=0
        while index<len(s):
            strings.append(s[index:index+i])
            index+=i
        count=1
        current=''
        for j in range(1,len(strings)):
            if strings[j]!=strings[j-1]:
                if count>1:
                    current=current+str(count)+strings[j-1]
                    count=1
                else:
                    current=current+strings[j-1]
            else:
                count+=1

        if count>1:
            current=current+str(count)+strings[-1]
        else:
            current=current+strings[-1]

        if len(current)<answer:
            answer=len(current)
            
    return answer
