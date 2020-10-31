#프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/17681

def change(n,array):
    for i in range(len(array)):
        changed=str(bin(array[i]))[2:]
        if len(changed)<n:
            changed='0'*(n-len(changed))+changed
        array[i]=changed
    return array
        

def solution(n, arr1, arr2):
    answer = []
    arr1=change(n,arr1)
    arr2=change(n,arr2)
    
    for i in range(n):
        answer.append('')
        for j in range(n):
            if arr1[i][j]=='1' or arr2[i][j]=='1':
                answer[i]+='#'
            else:
                answer[i]+=' '
    
    return answer
