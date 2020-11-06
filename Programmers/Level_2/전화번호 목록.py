#프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                answer=False
                break
        if answer==False:
            break
    return answer
