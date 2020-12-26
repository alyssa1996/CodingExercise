def icecreamParlor(m, arr):
    for i in range(len(arr)):
        if m-arr[i] in arr[i+1:]:
            return (i+1,(arr[i+1:].index(m-arr[i]))+i+2)
            break
