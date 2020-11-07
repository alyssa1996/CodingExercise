def solution(dartResult):
    dart=list()
    index=0
    while index!=len(dartResult):
        current=dartResult[index]
        if current.isnumeric():
            if dartResult[index+1].isnumeric():
                dart.append(int(dartResult[index:index+2]))
                index+=2
            else:
                dart.append(int(current))
                index+=1
            continue
        if current=='D':
            dart[-1]**=2
        elif current=='T':
            dart[-1]**=3
        elif current=='*':
            dart[-1]*=2
            if len(dart)!=1:
                dart[-2]*=2
        elif current=='#':
            dart[-1]=(-dart[-1])
        index+=1
    return sum(dart)
