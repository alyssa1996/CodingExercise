# Not Boring Movies

### 문제
문제 출처: https://leetcode.com/problems/not-boring-movies/
<br></br>

### 문제풀이법
문제에 제시된 조건들을 다 적용하면 해결할 수 있는 문제.
```mysql
select *
from Cinema
where id % 2 = 1 and description != "boring"
order by rating desc
```
* 처음으로 sql 구문 쓸 때도 나머지 기호가 '%'라는 것을 알게 되었고, 'is not'이라는 구문을 쓸 수 없고 '!='를 써야 한다는 것을 알게 되었다.