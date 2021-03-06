## 소수 찾기
'소수찾기' 문제를 처음 접하여 접근한 풀이 방식으로는 효율성 채점 기준을 통과할 수 없었다. 여러가지 방법으로 혼자 시도해도 효율성은 좀처럼 나아지지 않았다. 
그래서 다른 사람들이 문의한 게시판을 보다가 [**에라토스테네스의 체**](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
라는 알고리즘을 적용하여 문제를 풀면 효율성이 현저히 좋아진다는 것을 배웠다. <br>
#### **"에라토스테네스의 체"** 접근방식
1. 에라토스테네스의 체를 이용해 1~n까지의 소수를 알고 싶다면, n까지 모든 수의 배수를 다 나눠 볼 필요는 없다. 만약 어떤 수 *m=ab*라면 a와 b 중 적어도 하나는 n의 제곱근 이하이다. 
즉 n보다 작은 합성수 m은 n의 제곱근보다 작은 수의 배수만 체크해도 전부 지워진다는 의미이므로, n의 제곱근 이하의 수의 배수만 지우면 된다.[1](https://namu.wiki/w/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%20%EC%B2%B4)
2. i가 소수라면, n에 포함된 i의 배수들은 소수일 수 없으므로 i*2부터 n까지의 i의 배수들은 모두 제외한다.
