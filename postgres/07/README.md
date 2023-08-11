# 정렬하기

`ORDER BY` 키워드로 가능하다.

ascending이 기본이고, `DESC` 키워드를 붙이면 descending으로 쿼리한다

## ORDER BY 사용법

1. 기본사용은 설명완료함
2. `ORDER BY price, weight DESC` 이런식으로 차례로 순서를 기재해줄 수 있다.

## `OFFSET`, `LIMIT`에 대해

id 부터 얼마만큼 offset을 계산해서 갖고온다 (integer나 bigint만 될듯하다)

[참고링크](https://www.postgresql.org/docs/current/queries-limit.html)

```sql
select
  name
from
  phones
order by
  price desc
limit
  2 offset 1;
```
