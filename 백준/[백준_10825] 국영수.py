'''
def sorting(a,b,start,index,scores):
    while index<len(students):
        if students[index][a]==students[index-1][a]:
            scores.append(students[index])
        else:
            if b==2:
                scores.sort(key=lambda score:score[b])
            elif b==3:
                scores.sort(reverse=True, key=lambda score:score[b])
            students[start:start+len(scores)]=scores
            scores.clear()
            scores=[students[index]]
            start=index
        index+=1
        
    if b==2:
        scores.sort(key=lambda score:score[b])
    elif b==3:
        scores.sort(reverse=True, key=lambda score:score[b])
    students[start:start+len(scores)]=scores
'''

n=int(input())
students=[]
for i in range(n):
    name,kor,eng,math=input().split()
    students.append((name,int(kor),int(eng),int(math)))

'''
students.sort(reverse=True, key=lambda score:score[1])
sorting(1,2,0,1,[students[0]])
sorting(2,3,0,1,[students[0]])
'''

students.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(students[i][0])
