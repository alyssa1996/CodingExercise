#프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer+=(A[i]*B[len(B)-1-i])
    return answer
