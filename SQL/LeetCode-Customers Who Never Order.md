# Customers Who Never Order

### 문제
문제 출처: https://leetcode.com/problems/customers-who-never-order/
<br></br>

### 문제풀이법
주문을 한 적이 있는 고객의 아이디들을 골라내고, 그 안에 아이디가 없는 고객에 한해 이름을 추출하는 방식으로 접근
```myspl
select Name as Customers
from Customers
where Id not in (
    select Customers.Id 
    from Customers, Orders 
    where Customers.Id = Orders.CustomerId
)
```