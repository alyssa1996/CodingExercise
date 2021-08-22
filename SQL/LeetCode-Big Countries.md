# Big Countries

### 문제
문제 출처: https://leetcode.com/problems/big-countries/
<br></br>

### 문제풀이법
조건 둘 중 하나에 해당하는 경우 모두 고르도록 해결
```mysql
select name, population, area
from World
where population > 25000000 or area > 3000000
```
