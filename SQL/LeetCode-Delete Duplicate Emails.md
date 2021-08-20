# Delete Duplicate Emails

### 문제
문제 출처: https://leetcode.com/problems/delete-duplicate-emails/
<br></br>

### 문제풀이법
Person table을 join하여 이메일은 같고, id는 큰 값들을 삭제하는 방식으로 접근
```mysql
#방법1
Delete t1 from Person t1
Join Person t2
on t1.Email = t2.Email
where t1.Id > t2.Id
```
```mysql
#방법2
Delete t1 
from Person t1, Person t2
where  t1.Email = t2.Email and t1.Id > t2.Id
```