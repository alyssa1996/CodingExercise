n=int(input())
students=[]
for i in range(n):
    name,score=input().split()
    students.append((name,int(score)))

def getScore(data):
    return data[1]

students.sort(key=getScore)
for i in range(n):
    print(students[i][0],end=' ')
