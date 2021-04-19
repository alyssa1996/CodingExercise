# CodingExercise
Study Algorithm

## Python 요약집
### #1 sorted()와 sort()의공통점과 차이점
**차이점**
1. sorted()의 경우, 원본을 바꾸지 않는다. 그리고 iterable한 데이터 타입(ex. 사전, 튜플 등)에도 사용가능하다.
2. sort()의 경우, 원본 자체가 바뀐다. 하여 리스트 타입에만 사용가능하다.

**공통점**
1. key=<function>을 통해 정렬 기준을 임의 설정할 수 있다.
2. reverse=True/False를 통해 오름차순/내림차순을 통제할 수 있다.

### #2 eval() 함수
eval()은 매개변수로 '식'을 문자열 형태로 받아와 그 식의 실행값(결과값)을 리턴해주는 함수이다.<br>
두 번째 예시와 같이 함수또한 포함하여 계산할 수 있다. ([그외 자세한 정보](https://blockdmask.tistory.com/437))
```python
eval('3+5')
>>> 8

eval('abs(-2-8)')
>>> 10
```
Off the record: 이 함수를 알게된 것은 [2020 카카오 인턴십 수식최대화](https://programmers.co.kr/learn/courses/30/lessons/67257) 문제를 풀면서였다. 나는 수식 계산을 위해 문자열 내 숫자도 int형으로 변경해주고, 계산을 위해 함수도 따로 만들었는데, 다른 사람들의 풀이에는 그 과정이 보이지 않아 유심히 살펴보니 그들은 이 함수를 활용하고 있었다. 이를 통해 한 가지 더 배웠다!
