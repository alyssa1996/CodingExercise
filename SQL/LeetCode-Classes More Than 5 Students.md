#Classes More Than 5 Students

### 문제
문제 출처: https://leetcode.com/problems/classes-more-than-5-students/
<br></br>

### 문제풀이법
같은 class로 묶어서 그 class를 듣는 학생의 수가 5명 이상인지 확인하여 class 명을 추출하는 방식으로 접근.
```mysql
select class
from courses
group by class having count(distinct student) >= 5
```
* 처음 풀었을 때는 distinct를 사용하지 않고, 풀어서 중복으로 들어간 학생의 이름도 각각 카운트되어 틀렸었는데, distinct를 통해 중복값을 없애자 정답이 되었다!