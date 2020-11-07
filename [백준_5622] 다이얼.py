numbers=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],
         ['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
words=input("")

time=0
for i in words:
    for j in range(len(numbers)):
        if i in numbers[j]:
            time=time+j+3
print(time)
         
