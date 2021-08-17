# Second Highest Salary

### 문제
![image](https://user-images.githubusercontent.com/40799546/129809922-32e21845-1d56-4e18-93fc-484c10832898.png)
문제 출처: https://leetcode.com/problems/second-highest-salary/
<br></br>

### 문제풀이법
먼저 가장 큰 값을 찾아서 그 최대값보다 작은 Salary 중에서 가장 큰 값(결국 두 번째로 큰 값)을 찾는 방식으로 접근
```mysql
select Max(Salary) as SecondHighestSalary
from Employee
where Salary < all ( select Max(Salary) from Employee )
```
