'''여기서 핵심은 answer.sort(key=lamba x: x*3,reverse=True)라고 생각한다.
가장 이해가 안가는 부분이기도 하고....
일단 key를 사용하면 정렬할 기준을 설정할 수 있다고 한다.
예를 들어 여러 단어들이 담긴 리스트가 있다고 가정했을 때 만약 단어의 길이를 기준으로
리스트를 정렬하고 싶다면, list.sort(key=lambda x:len(x) 처럼 작성해야한다.
즉 이 문제에서는 x*3을 기준으로 정렬하기로 한거고, x*3인 이유는 문제 조건에서
numbers의 원소가 1000이하의 숫자라고 했기 때문이다.
이렇게 정렬한 것을 다시 reverse=True를 하는 이유는 올림차순 된 것을 내림차순으로
바꿔야 가장 큰 수가 되기 때문이다.
그렇게 해서 answer에 리턴되는 것은 key에 따라 정렬되고, 다시 그 정렬된 것이
내림차순으로 정리된 numbers의 원소들인 것이다.
'''

def solution(numbers):
    answer = list(map(str,numbers))
    answer.sort(key=lambda x: x*3,reverse=True)
    return str(int(''.join(answer)))
