# Join에 대해 파봅시다

한 테이블에 여러 외래키를 두는경우로 학습해보기로 한다.

## JOIN과 AGGREGATION에 대해

- Join: 필요한 값에 대해 관계를 통하여 가져옴
- Aggregation: 쿼리한 값에 대해 연산결과를 구하는 과정

## JOIN 해보기 (1)

[공식문서](https://www.postgresql.org/docs/current/tutorial-join.html)도 살펴보세요~

다른테이블로부터 JOIN 하는 방안

```sql
SELECT
  contents,
  username
FROM
  COMMENTS
  JOIN users on users.id = comments.user_id;
```

## JOIN을 짤 때

- `FROM` 구문, `JOIN` 구문의 순서로 인해 쿼리가 다르게 될 수 있다
  - JOIN 순서에 따라서 쿼리가 될 수도 있고 안될 수도 있다.
    - `LEFT OUTER JOIN`을 하는데 대상이 되는 테이블을 다르게 지정하더라도 쿼리가 될 수 있음
- 컬럼 이름이 겹치면 컨텍스트를 전달해야한다.
  - 그래서 이름을 잘 지어줘야함. 설계부터 뭐가 뭐에 엮이고 할 것인지 잘 생각해야하는 것이 그 이유다.
- 테이블은 `AS` 키워드로 이름을 다르게 줄 수 있다
- JOIN의 종류는 여러가지다.

## JOIN의 종류

JOIN 시 `null` 값을 넣어놓고 그 값까지 JOIN으로 쿼리하도록 하면 안 나온다! `INNER JOIN` 이 기본값이라 쿼리가 안된듯하다.

두 테이블을 합칠 때의 조건을 지정해줄 수 있음. 이 강의에서는 4가지 JOIN을 소개해줌.

### `INNER JOIN`?

- 기본값!
- 두 테이블 모두에서 겹치는 값을 갖고옴

### `LEFT OUTER JOIN`?

- `LEFT JOIN` 이라는 키워드를 붙이면 됨
- `FROM` 구문으로 가리키는 테이블에 대해 가져옴

### `RIGHT OUTER JOIN`?

- `RIGHT JOIN` 이라는 키워드를 붙이면 됨
- `FROM` 구문으로 가리키지 않는 테이블에 대해 가져옴

### `FULL JOIN`?

- `FULL JOIN` 이라는 키워드를 붙이면 됨
- 연관있는 값이건 아니건 모두 가져옴
- 없는값은 `null` 로 처리함

## JOIN 과 동시에 WHERE를 쓰면?

JOIN 구문 다음에 쓴다. JOIN은 그냥 `FROM` 안에 포함된다고 생각하자

## three way joins

세 테이블에 대해 그냥 join을 하면 셋 다 있는 값에 대해서만 나올 것임. 기본값이 `INNER JOIN` 이니..

같이 JOIN하기 위해 하단 JOIN에는 AND 구문으로 추가 관계를 풀어주었다.

```sql
SELECT
  url,
  contents,
  users.username
FROM
  comments
  JOIN photos ON photos.id = comments.photo_id
  JOIN users ON users.id = comments.user_id
  AND users.id = photos.user_id
WHERE
  comments.user_id = photos.user_id;
```
