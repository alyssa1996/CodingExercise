def solution(numbers, hand):
    answer = ''
    phone=[[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    left_po,right_po=[0,3],[2,3]
    for i in numbers:
        if i in phone[0]:
            left_po=[0,phone[0].index(i)]
            answer+='L'
        if i in phone[1]:
            target=[1,phone[1].index(i)]
            left_dis=abs(left_po[0]-target[0])+abs(left_po[1]-target[1])
            right_dis=abs(right_po[0]-target[0])+abs(right_po[1]-target[1])
            if left_dis<right_dis:
                left_po=target
                answer+='L'
            elif right_dis<left_dis:
                right_po=target
                answer+='R'
            else:
                if hand=="right":
                    right_po=target
                    answer+='R'
                else:
                    left_po=target
                    answer+='L'
        if i in phone[2]:
            right_po=[2,phone[2].index(i)]
            answer+='R'
    return answer
