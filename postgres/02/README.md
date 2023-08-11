# 레코드 필터링

### 조건을 걸려면?

```sql
SELECT name, area FROM cities WHERE area > 4000;

-- 좀더 복잡하게...
SELECT
	name,
	population / area AS population_density
FROM
	cities
WHERE
	population / area > 6000;
```

#### 비교를 위한 오퍼레이터는?

* 등호(들)
* NOT EQUAL은 표현방식이 두개다.
  * `<>`
  * `!=`
* `BETWEEN` 은 두 값 사이에 값이 있는가?
* `IN` 은 리스트 안에 값이 있는가?
* `NOT IN`은 리스트 안에 값이 **없는가**?

### 값을 수정하려면?

```sql
-- WHERE 절 없으면 모든 구문을 업데이트함!!!!!!!!
UPDATE
    cities
SET population = 39500000
WHERE
    name = 'Tokyo';
```



### 값을 지우려면?

```sql
-- WHERE 절 없으면 모든 구문을 지운다!!!!!!!!!!
DELETE FROM cities
WHERE
    name = 'Tokyo';
```

