def checkMagazine(magazine, note):
    dic=dict()
    for i in magazine:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    
    result=True
    for j in note:
        if j in dic.keys():
            dic[j]-=1
            if dic[j]==0:
                del dic[j]
        else:
            result=False
            break
    
    if result:
        print("Yes")
    else:
        print("No")
