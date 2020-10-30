#https://codeup.kr/problem.php?id=4011
start,end=input("").split("-")

if start[0] in [3,4]:
    year='20'
else:
    year='19'

birthday=year+start[:2]+"/"+start[2:4]+"/"+start[4:6]

if end[0] in ['1','3']:
    gender='M'
else:
    gender='F'

print("%s %s"%(birthday,gender))
