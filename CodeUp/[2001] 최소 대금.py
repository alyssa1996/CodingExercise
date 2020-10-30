#코드업 https://codeup.kr/problem.php?id=2001

pasta=list()
juice=list()
for i in range(3):
    pasta.append(int(input("")))

for i in range(2):
    juice.append(int(input("")))
    
total=min(pasta)+min(juice)
print("%.1f"%(total+(total*0.1)))
