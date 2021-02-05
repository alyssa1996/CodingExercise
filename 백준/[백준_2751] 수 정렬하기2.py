n=int(input())

array=list()
for i in range(n):
    array.append(int(input()))

array.sort()
for i in array:
    print(i)
