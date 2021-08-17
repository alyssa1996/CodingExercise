# Second Highest Salary

문제 출처: https://leetcode.com/problems/second-highest-salary/
<br></br>
```myspl
select Max(Salary) as SecondHighestSalary
from Employee
where Salary < all ( select Max(Salary) from Employee )
```