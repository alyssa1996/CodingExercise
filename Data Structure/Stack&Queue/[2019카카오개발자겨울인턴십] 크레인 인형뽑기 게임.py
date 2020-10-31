#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket=list()
    for i in moves:
        for j in board:
            if not j[i-1] == 0:
                if len(basket)==0:
                    basket.append(j[i-1])
                elif basket[-1] ==j[i-1]:
                    answer+=1
                    basket.pop()          
                else:
                    basket.append(j[i-1])
                j[i-1]=0
                break
    return answer*2
