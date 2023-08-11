# PostgreSQL 입문

데이터베이스: 디스크에 값을 넣고 주기적으로 가져오게 할 수 있는 서비스

SQL: DB로부터 값을 추가/읽기/수정/삭제 할 수 있도록 하는 구문

DB 잘 다루는 방법

- 값을 효율적으로 꺼내는 쿼리 잘짜기
- 스키마, DB구조 설계 잘하기
- 필요한 고급요소(advanced features) 들은 어떤게 있는지 이해하기
- 프로덕션 환경에서 DB 운영 잘하기

## DB 디자인

[이 링크](https://en.wikipedia.org/wiki/List_of_largest_cities)를 가지고 설계를 해보자! 간단한건 [여기서](https://pg-sql.com/) 구동 테스트 해보자

1. 각 도시별 **어떤 값**을 저장할 것인지 살펴보자 → 테이블 설계
   1. "도시 정보"
2. 1의 값은 어떤 **프로퍼티**를 갖고있는지 알아보자 → 컬럼 설계 (1)
   1. 이름, 국가, 인구, 크기
3. 2의 값들은 어떤 **타입**의 데이터로 저장되는지 알아보자 → 컬럼 설계 (2)
   1. string, string, number, number

### 테이블 만들기

```sql
CREATE TABLE cities (
  name VARCHAR(50),
  country	VARCHAR(50),
  population INTEGER,
  area INTEGER
);
```

- 키워드(Keywords): 뭐 해라고 하는 명령어 (대문자로 쓰세요)
- 식별자(Identifiers): 어느 테이블이나 컬럼처럼, 어디서 일해라고 지시할 때 쓰는 식별값 (소문자로 쓰세요)
- 컬럼: 어떤 식별자로 어떤 값이 저장될지에 대한 정의
  - 데이터 타입: 저장될 데이터에 대한 타입
  - 식별자: 상동

### 테이블에 값 추가하기

```sql
INSERT INTO cities (name, country, population, area)
VALUES ('Tokyo', 'Japan', 38505000, 8223);

-- 여러 줄을 넣으려면?
INSERT INTO cities (name, country, population, area)
VALUES
    ('Dehli', 'India', 28125000, 2240),
    ('Shanghai', 'China', 22125000, 4015),
    ('Sao Paulo', 'Brazil', 20935000, 3043);
```

- 컬럼명과 값이 확실히 겹쳐지는지 확인하기

### 테이블에서 값 살펴보기

```sql
-- 다 보고싶으면?
SELECT * FROM cities;

-- 일부만 보고싶으면?
SELECT name, country FROM cities;

-- 하나를 여러번보는 것도 되긴함
SELECT name, name, name FROM cities;
```

### 계산된 결과가 쿼리되게 하려면?

```sql
SELECT name, population / area FROM cities;

-- 컬럼을 이름을 정해주려면
SELECT
	name,
	population / area AS density
FROM cities;
```

- 수학 계산을 하는 오퍼레이터는...
  - `+`
  - `-`
  - `*`
  - `%`
  - `^`
  - `|/` (제곱근)
  - `@` (절대값)

### 문자열을 연산하는 함수, 오퍼레이터는...

- `CONCAT()`
- `||`
- `LENGTH()`
- `UPPER()`
- `LOWER()`

```sql
SELECT name || ',' || country as location FROM cities;

-- is equivalent to...
SELECT CONCAT(name, ',', country) AS location FROM cities;

-- 추가로...
SELECT UPPER(CONCAT(name, ',', country)) AS location FROM cities;
```
