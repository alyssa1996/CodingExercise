# Big Countries

### 문제
문제 출처: https://leetcode.com/problems/reformat-department-table/
<br></br>

### 문제풀이법
```mysql
select id,
 sum(case when month = 'Jan' then revenue end) as 'Jan_Revenue',
 sum(case when month = 'Feb' then revenue end) as 'Feb_Revenue',
 sum(case when month = 'Mar' then revenue end) as 'Mar_Revenue',
 sum(case when month = 'Apr' then revenue end) as 'Apr_Revenue',
 sum(case when month = 'May' then revenue end) as 'May_Revenue',
 sum(case when month = 'Jun' then revenue end) as 'Jun_Revenue',
 sum(case when month = 'Jul' then revenue end) as 'Jul_Revenue',
 sum(case when month = 'Aug' then revenue end) as 'Aug_Revenue',
 sum(case when month = 'Sep' then revenue end) as 'Sep_Revenue',
 sum(Case when month = 'Oct' then revenue end) as 'Oct_Revenue',
 sum(case when month = 'Nov' then revenue end) as 'Nov_Revenue',
 sum(Case when month = 'Dec' then revenue end) as 'Dec_Revenue'
 from Department
 group by id
```

* 사람들의 답안을 참고해서 풀기는 풀었는데, 왜 sum이나 max를 붙여야 하는지 잘 모르겠다. 아무래도 group by로 묶어 버려서 그런 것 같기는 한데....
