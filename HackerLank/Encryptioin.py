def encryption(s):
    length=(len(s)**(1/2))
    column=int(length);row=column+1
    if column*(row-1)==len(s):
        row-=1
    if column*row<len(s):
        column+=1
        
    array=list();index=0
    for i in range(column):
        array.append(list(s[index:index+row]))
        index+=row
    
    print(array)
    result=list()
    for i in range(row):
        for j in range(column):
            if len(array[j])>i:
                result.append(array[j][i])
        result.append(' ')
    
    return ''.join(result)
