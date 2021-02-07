from sys import stdin

n=int(stdin.readline())

students=dict()
for i in range(n):
    age,name=stdin.readline().split()
    if int(age) in students.keys():
        students[int(age)].append(name)
    else:
        students[int(age)]=[name]

sorted_students=sorted(students)
for age in sorted_students:
    for j in range(len(students[age])):
        print(age,students[age][j])
