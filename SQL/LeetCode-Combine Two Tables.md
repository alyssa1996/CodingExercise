# Big Countries

### 문제
문제 출처: https://leetcode.com/problems/combine-two-tables/
<br></br>

### 문제풀이법
left join을 이용하여 왼편이 있는 Person을 기준으로 on conditions에 match되는 Address 값은 가져오고 없으면 null 채워버리는 방법(답안지 보고 해결)
```mysql
Select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
```
