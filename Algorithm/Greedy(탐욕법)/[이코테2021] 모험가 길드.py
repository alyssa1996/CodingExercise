n=int(input())
members=sorted(list(map(int,input().split())))

if members[-1]==n:
    print(1)
else:
    group=0
    while len(members):
        members,n=members[:n-(members[-1])],n-(members[-1])
        group+=1
    print(group)


#모범 답안
    
result=0 #총 그룹의 수
count=0 #현재 그룹에 포함된 모헙가의 수
for i in members: #공포도가 낮은 것부터 하나씩 확인하며
    count+=1 #현재 그룹에 해당 모험가를 포함시키기
    if count>=i: #현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹 결성
        result+=1 #총 그룹의 수 증가시키기
        count=0 #현재 그룹에 포함된 모험가의 수 초기화

print(result)
