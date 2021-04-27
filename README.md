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


### #3 defaultdict()
defaultdict()는 딕셔너리를 만드는 dict 클라스의 서브 클라스라고 한다.<br>
defaultdict()를 사용하면 인자로 주어진 객체의 기본값을 딕셔너리 값의 초기값으로 설정할 수 있다.<br>
이 함수를 이용하면 딕셔너리 내에 없던 key를 호출해도 설정된 초기값으로 자동 초기화되기 때문에, 불러오고 싶은 key가 딕셔너리에 있는지 없는지 확인하지 않아도 된다는 장점이 있다. 
```python
# defaultdict()를 사용하지 않은 경우
word="this is example"
dictionary=dict()

for value in word:
	if value in dictionary:
		dictionary[value]+=1
	else:
		dictionary[value]=1

print(dictionary)
>>> {'t': 1, 'h': 1, 'i': 2, 's': 2, ' ': 2, 'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}
```
```python
# defaultdict()를 사용하는 경우
from collections import defaultdict # 단 반드시 import
word="this is example"
dictionary=defaultdict(int)

for value in word:
	dictionary[value] += 1 # 초기화 없이 바로 연산하는 것도 가능하다

print(dictionary)
>>> {'t': 1, 'h': 1, 'i': 2, 's': 2, ' ': 2, 'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}
```
이처럼 defaultdict()를 사용하면 코드가 한결 깔끔해지고, 구현하는 데에도 편리한 것을 확인할 수 있다. 인자로 list,set등도 받을 수 있기 때문에 더 복잡한 구현도 defaultdict()를 이용하면 더욱 손쉬 질 것이라고 예상된다!
* 참고 사이트: https://dongdongfather.tistory.com/69 , https://itholic.github.io/python-defaultdict/
