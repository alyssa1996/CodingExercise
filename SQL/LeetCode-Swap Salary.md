# Swap-salary

### 문제
문제 출처: https://leetcode.com/problems/swap-salary/
<br></br>

### 문제풀이법
sex 속성의 값이 'm이면 'f'로, 그렇지 않으면(즉, 'f'였으면) 'm'으로 바꾸도록 if문 등을 사용하여 해결하는 방법
```mysql
#방법1
update Salary
set sex = if(sex = 'm', 'f', 'm')
```
```mysql
#방법2
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
```
* 처음으로 update문을 사용해보는 문제였다. 결국 답을 보고 해결한 경우였는데, 도저히 swap하는 방법이 떠오르지 않았기 때문이다. 답에는 위와 같이 두 경우가 있었는데, 첫번째가 더 직관적이고 단순하다고 생각했다. 그리고 ```CASE ... WHEN ...``` 구문으로 처음 봤는데, 이 경우에는 조건이 3개 이상일 때 더 유용하다고 생각한다. 파이썬으로 치면 ```if elif else``` 구문처럼!
