def create_list(string):
    new=[]
    for i in range(len(string)-1):
        current=string[i:i+2]
        if current.isalpha():
            new.append(string[i:i+2])
    return new

def solution(str1, str2):
    INT=65536
    set1=sorted(create_list(str1.lower()))
    set2=sorted(create_list(str2.lower()))

    if len(set1)==0 and len(set2)==0:
        return INT
    
    inter=[]
    union=[]
    index=0
    while index<len(set1):
        current=set1[index]
        if current in set2:
            inter.append(current)
            del set2[set2.index(current)]
            del set1[set1.index(current)]
        else:
            index+=1
    union=inter+set1+set2

    return int((len(inter)/len(union))*INT)
