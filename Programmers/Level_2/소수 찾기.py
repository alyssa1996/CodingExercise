from itertools import permutations

def solution(numbers):
    answer = 0
    n=list(map(int,list(numbers)))
    all_case=[]
    for i in range(len(n)):
        if n[i]==1 or n[i]==0:
            continue
        all_case.append(n[i])
    
    all_case=list(set(all_case))
    for i in range(2,len(n)+1):
        result=list(set(list(permutations(n,i))))
        for j in range(len(result)):
            if result[j][0]==0:
                continue
            temp=list(map(str,result[j]))
            all_case.append(int(''.join(temp)))
    
    for i in range(len(all_case)):
        check=True
        num=all_case[i]//2
        while True:
            if num==1:
                break
            if all_case[i]%num==0:
                check=False
                break
            else:
                num-=1
        if check:
            answer+=1
            
    return answer
