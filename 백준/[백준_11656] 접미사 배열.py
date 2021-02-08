from sys import stdin

sentence=stdin.readline().strip()
part=[0]*len(sentence)
for i in range(len(sentence)):
    part[i]=sentence[i:]

part.sort()
for i in part:
    print(i)
