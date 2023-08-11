# Union과 Sets을 사용한 Intersections 표기

(`쿼리`) UNION (`쿼리`)

형식으로 UNION을 할 수 있다.

두 쿼리를 수행하여 하나의 결과를 받아봐야할 때 쓴다. 기본값으로 호출하면 중복도 없어진다.

하지만, 동일 컬럼, 동일 값에 대해 쿼리해야한다는 조건이 있다.

`UNION ALL` 키워드를 쓰면 중복을 포함한다.

## 다른 키워드 소개

이런 관계를 표현하는 키워드가 PostgreSQL에는 더 있다

| 키워드명        | 상세                                                                  | 중복제거 |
| --------------- | --------------------------------------------------------------------- | -------- |
| `UNION`         | 두 쿼리 결과를 합친다                                                 | 예       |
| `UNION ALL`     | 두 쿼리 결과를 합친다                                                 | 아니오   |
| `INTERSECT`     | 두 쿼리 결과에서 교집합 결과를 가져온다                               | 예       |
| `INTERSECT ALL` | 두 쿼리 결과에서 교집합 결과를 가져온다                               | 아니오   |
| `EXCEPT`        | 두 쿼리 결과에서 **차집합 결과** 를 가져온다 (두번째 쿼리결과를 제외) | 예       |
| `EXCEPT ALL`    | 두 쿼리 결과에서 **차집합 결과** 를 가져온다 (두번째 쿼리결과를 제외) | 아니오   |

[공식문서 참고하기](https://www.postgresql.org/docs/current/queries-union.html)

```sql
(
  SELECT *
  FROM products
  ORDER BY price DESC
  LIMIT 4
)
UNION
(
  SELECT *
  FROM products
  ORDER BY price / weight DESC
  LIMIT 4
);
```

이 쿼리를 기반으로 살펴보자

```sql
SELECT
  manufacturer
FROM
  phones
WHERE
  price < 170
UNION
SELECT
  manufacturer,
  COUNT(*)
FROM
  phones
GROUP BY
  manufacturer
HAVING
  COUNT(*) > 2
```

두 쿼리를 이렇게 하면 결과에 대해 머지가 됨
