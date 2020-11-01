number=int(input(""))

people=list()
for i in range(number):
    people.append(input("").split(" "))

for i in range(len(people)):
    people[i].append(0)
    for j in range(len(people)):
        if i==j:
            continue
        if people[i][1]<people[j][1] and people[i][0]<people[j][0]:
            people[i][2]+=1

for i in people:
    print(i[2]+1,end=' ')


