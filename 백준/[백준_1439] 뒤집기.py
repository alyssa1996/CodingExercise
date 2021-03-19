s=input()
result=[s[0]]

for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        result.append(s[i])

count_0=result.count('0')
count_1=result.count('1')
print(min(count_0,count_1))
