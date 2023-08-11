# 테이블을 갖고 작업해보기

## 들어가며

하나의 테이블에 모든 작업을 하는 일은 거의없다.

따라서 여러 테이블과 관계를 맺고 값을 표현하는 작업이 필요하다.

## 테이블 디자인

사진 공유와 관련한 애플리케이션을 만든다고 가정해보자. 그렇다면 필요한 테이블은 대충 아래와 같이 있을 것이다:

- `users`
- `photos`
- `comments`
- `likes`

### 어떤 테이블을 만들까?

- 일반적인 feature들은 전통적인 테이블명과 컬럼으로 쉽게 만들어진다. (인증, 댓글, 등등 누구든 구현했을 만한 것들)
- 어떤 종류의 리소스가 앱에 존재하는지를 살펴보고, 이를 토대로 기능별로 테이블을 만들어야 한다.
- feature들은 테이블 디자인으로부터 반영되는 리소스의 두 형태, "관계"나 "오너쉽"을 가리키는 것 처럼 보인다.

### 인스타라고 쳤을 때?

- 유저(팔로워, 팔로잉)
- 프로필(유저의 프로필)
- 사진 리스트들
  - 사진엔 '좋아요'를 할 수 있다
  - '댓글'을 '유저'가 달 수 있다

### 관계를 잡아봅시다

- 뭐는 뭘 하고 뭐는 뭘 가진다 하는 설계를 한다
- 학교에서 배운 ER Diagram으로 추려내면 될 것이다

## 일대일, 일대다, 다대다?

### 일대다(One-to-Many)? 다대일(Many-to-One)?

- 일대다?
  - '유저'는 '사진' '여럿을' 가질 수 있다
- 다대일?
  - '사진'은 '한명의' 유저를 가질 수 있다
  - '유저'들은 '사진'에 '좋아요'를 할 수 있다.
  - 사진에 '유저들'은 댓글을 달 수 있다.

### 일대일(One-to-One)?

- 뭐 하나가 단 하나의 객체와만 관게를 맺는 것

### 다대다?

- 어떤 개념이 여러 개념과 연계지을 수 있는 것을 의미

## Primary Keys, Foreign Keys

### 주 키

- 테이블에서 값을 식별할 수 있는 유일한 레코드
  - 모든 테이블에 하나는 있어야됨
  - 보통 `id` 를 씀
  - UUID 를 쓰기도 함
  - 바뀌면 안됨

### 외래 키

- "관계"로 묶인 필드를 참조할 수 있는 레코드
  - 다른 레코드에 속하는 로우
  - 테이블에 동일한 foreign key를 가리키는 로우가 있을 수 있다
  - 보통 `<table>_id` 라는 이름을 가짐 (이걸 잘 해야 "`id` is ambiguous"같은 에러를 방지할 수 있다) (처음 디비설계부터 제대로 되어야함을 암시한다고 생각한다)
  - 남의 PK값과 동일함
  - 관계가 바뀌면 바뀔 수도 있음

## 본격적인 설계

- comments

  - id(pk)
  - text
  - user_id(fk)
  - photo_id(fk)

- photos

  - id(pk)
  - url
  - user_id(fk)

- users
  - id(pk)
  - username
  - email

## 테이블 생성

### key 값?

`SERIAL` 태그로 auto-increment 설정

### 외래키?

`REFERENCES` 키워드 사용. `REFERENCES <table_name>(id_name)` 과 같은 방식으로..

E.g,

```sql
CREATE TABLE photos(
    id SERIAL PRIMARY KEY,
    url VARCHAR(200),
    user_id INTEGER REFERENCES users(id)
);
```

## 연관있는 값을 쿼리하려면?

```sql
SELECT url, username
FROM photos
JOIN users ON users.id = photos.user_id;
```

## 테이블에 값 추가?

외래키로 엮여있음에도 값을 추가하고 싶다면?

null 추가를 가능하게 하든가, 그것도 막든가

## 테이블에서 값 제거?

외래키를 묶고 지우려면 아래 삭제 옵션을 달아서 처리한다.

| 삭제옵션                | 상세                                        |
| ----------------------- | ------------------------------------------- |
| `ON DELETE RESTRICT`    | 에러 리턴 시킴                              |
| `ON DELETE NO ACTION`   | 에러 리턴 시킴(참고: 기본값임)              |
| `ON DELETE CASCADE`     | 연관있는 값을 같이 지움                     |
| `ON DELETE SET NULL`    | 연관있는 값의 FK값을 `null`로 바꿈          |
| `ON DELETE SET DEFAULT` | 연관있는 값의 FK값을 지정된 기본값으로 바꿈 |

---

- 예시값

```sql
CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  username VARCHAR(50)
);

CREATE TABLE photos (
  id SERIAL PRIMARY KEY,
  url VARCHAR(200),
  user_id INTEGER REFERENCES users(id)
);

INSERT INTO photos (url, user_id)
VALUES
('http:/one.jpg', 4),
('http:/two.jpg', 1),
('http:/25.jpg', 1),
('http:/36.jpg', 1),
('http:/754.jpg', 2),
('http:/35.jpg', 3),
('http:/256.jpg', 4);
```
