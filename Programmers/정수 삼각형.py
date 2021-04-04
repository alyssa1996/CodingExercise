def solution(triangle):
    answer = 0
    for line in range(1,len(triangle)):
        for i in range(len(triangle[line])):
            if i-1>=0:
                a=triangle[line-1][i-1]
            else:
                a=0
            if i<len(triangle[line-1]):
                b=triangle[line-1][i]
            else:
                b=0
            triangle[line][i]+=max(a,b)
    return max(triangle[-1])
