# Aggregation에 대해 공부해봅시다

레코드들을 연산한 결과를 하나로 축소한다.

## grouping vs. aggregates

- grouping
  - 많은 값을 여러 row로 축소한다
  - `GROUP BY` 키워드로 처리한다.
  - 결과를 줄이는게 사용의 핵심이다.
- aggregates
  - 많은 값을 하나의 값으로 축소한다.
  - aggregate functions으로 처리한다.

## 어떤 함수들이 있을까?

- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`

## 주의사항

Aggregation하면서 바로 쿼리할 수는 없다. 할거면 그룹별로 연산을 하기 위해 GROUP BY 그룹과 함께 사용해줘야한다.

## `GROUP BY`와 Aggregation을 동시에

그룹으로 묶은 값 내에 MAX 값을 따로 구해낸다.

그러면 그룹 내에서 aggregation한 값을 출력할 수 있다.

```sql
SELECT
  user_id,
  COUNT(id) as user_count
FROM
  comments
GROUP BY
  user_id;
```

## `COUNT()` 함수의 추가사항

- `COUNT()` 함수는 `null` 값을 세지 않는다.
  - `COUNT(user_id)` 라고 하면 user_id가 null값이면 안 센다
  - `COUNT(*)` 라고 하면 값이 있을 때 카운트하는 것이니...

```sql
SELECT
    authors.name,
    COUNT(*)
FROM
    authors
    JOIN books on authors.id = books.author_id
GROUP BY authors.name
```

## SQL 쿼리해석의 순서 (중요)

여태 수업을 봐왔으면 알겠지만, 지극히 당연한 이야기다.

| 키워드     | 해석순서 | 설명                                     |
| ---------- | -------- | ---------------------------------------- |
| `FROM`     | 1        | 어떤 테이블의 row에서 값을 가져올지 결정 |
| `JOIN`     | 2        | 다른 테이블과 값을 merge함               |
| `WHERE`    | 3        | row의 셋을 필터링함                      |
| `GROUP BY` | 4        | 유일한 값들의 모임으로 row를 그룹화한다  |
| `HAVING`   | 5        | 그룹의 모임을 필터한다                   |
| `ORDER BY` | 6        | 뽑혀나온 데이터를 정렬한다               |

## HAVING?

GROUP BY 한 그룹을 필터한다.

GROUP BY를 해야 HAVING을 할 수 있겠죠?

```sql
SELECT
  photo_id,
  COUNT(*)
FROM
  COMMENTS
WHERE
  photo_id < 3
GROUP BY
  photo_id
HAVING
  COUNT(*) > 2
```

GROUP_BY로 갖고올 값에 대해 HAVING절을 수행해야함에 유의

```sql
SELECT manufacturer, SUM(price * units_sold)
FROM phones
GROUP BY manufacturer
HAVING SUM(price * units_sold) > 2000000
```

## `HAVING` 구문의 추가사항

상기 쿼리해석 관련 내용에 더해...

GROUP BY, HAVING으로 묶을 수 없는 값은 쿼리할 수 없다.
