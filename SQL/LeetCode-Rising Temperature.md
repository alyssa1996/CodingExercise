# Rising Temperature

### 문제
문제 출처: https://leetcode.com/problems/rising-temperature/
<br></br>

### 문제풀이법
두 개의 Weather Table에 대해 날짜를 비교하여 날짜의 차이가 1이고, 전날 기온에 비해 오늘 기온이 높을 때만 id를 고르는 방식으로 접근
```mysql
select today.id
from Weather lastday, Weather today
where DATEDIFF(today.recordDate, lastday.recordDate) = 1 
and today.Temperature > lastday.Temperature
```

* 여기서 ```DATEDIFF()```를 처음 사용해보았다. 해설에 따르면 MySQL은 두 날짜의 값을 비교하기 위해 ```DATEDIFF()``` 함수를 사용한다고 한다.