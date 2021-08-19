# Employees Earning More Than Their Managers

### 문제
문제 출처: https://leetcode.com/problems/employees-earning-more-than-their-managers/
<br></br>

### 문제풀이법
Manager의 Salary를 찾아 그 값을 Employee의 Salary와 비교하여 Employee의 Salary가 더 클 때만 이름들을 추출하는데, 그 Field 명을 Employee로 명명
```mysql
select Name as Employee
from Employee as E
where Salary > (select Salary from Employee as M where E.ManagerId = M.Id)
```
