# Duplicate Emails

### 문제
문제 출처: https://leetcode.com/problems/duplicate-emails/
<br></br>

### 문제풀이법
같은 이메일로 그룹을 묶은 다음 그 이메일를 세었을 때, 그 갯수가 2개 이상인 이메일만 고르는 방법으로 접근
```mysql
select Email
from Person
Group By Email Having count(Email) > 1
```
