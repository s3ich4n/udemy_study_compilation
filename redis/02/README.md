# Redis 추가/쿼리 명령

## 추가

자료형에 따라 다르게 추가할 수 있다.

### Redis의 자료형

* String
* List
* Hash
* Set
* Sorted Set
* 등등...

## 들어가기에 앞서...

모든 명령어를 외우려는 미련한 짓은 하면 안 된다!

어떤 명령어가 어떤식으로 설계되었고, 왜 만들어졌는지를 이해해야 적재적소에 쓸 수 있다.

## 문자열을 살펴보자

대강 이런식의 명령어들이 있다:

![02-001-getters-and-setters-of-string](.\media\02_001.jpg)

### `SET` 을 살펴봅시다

* `SET <key> <value>`
* 나머지는 죄다 옵션
  * `|` 으로 OR을 표기한것
* Expire datetime도 정해줄 수 있음
  * 레디스를 캐싱서버로 쓸 때, 죄다 메모리 안에 넣어둘 수는 없으니 필요할 때는 레디스에서 서비스 해주다가 적당한 때에 만료와 동시에 원본을 갱신하는 전략을 취할 수 있음.
* `XX`, `NX` 옵션은 써봤음.
  * `XX`: Only set the key if it already exist.
  * `NX`: Only set the key if it does not already exist.

### 여러 키를 설정하는 방법

#### 기존 `SET`의 숏컷?

* `SETNX`: 없는 키값을 설정할 때만 `SET` 명령을 수행함
* `SETEX`: SET 하면서 expire time 설정해줌

#### 여러값을 동시에?

* `MSET`: key/value 쌍을 여러개 넣음
* `MSETEX`: key/value 쌍을 여러개 넣는데, expire time이 있음

### 여러 키를 가져오는 방법

* `MGET`: 여러 키값을 입력하면 값을 갖고옴
  * 없는 값은 `null` 을 리턴함

### 키를 지우려면?

* `DEL`
  * `DEL <key>`

### `GETRANGE`: range를 받고 문자열의 일부를 리턴

```bash
SET greeting 'hello there'
>>> 'OK'
GETRANGE greeting 0 3
>>> 'hell'
```

### `SETRANGE`: range를 받고 문자열의 일부를 수정

```bash
SET greeting 'hello there'
>>> 'OK'
SETRANGE greeting 3 aabb
>>> 11
GET greeting
>>> 'hellaabbhere'
```

### 근데 진짜 이런 명령어들을 다 쓸까요?

* 설계를 어떻게 하느냐에 따라서 빠른 실행의 명령으로 빠르게 데이터처리가 가능하다.
* 예시) 900억개 이상이 담긴 DB에서 조회할려니 속터지게 느린 관계로, 레디스를 써서 액세스, 업데이트 속도를 최대한 빠르게 해보시오
  * 전체값을 다 담기보다는 인코딩된 작은 값을 넣어서 저장하면?
  * 그걸 레디스에 담으면? (여기서부터 아이디어)
    * 그걸 꺼내고, 수정하는데 `GETRANGE`, `SETRANGE`, `MGET`, `MSET`을 쓰면 된다

## 숫자를 살펴보자

![02-002-getters-and-setters-of-number](.\media\02_002.jpg)

### 여기서의 `SET` 을 살펴봅시다

숫자를 넣더라도 문자열로 레디스에 저장된다.

### 숫자값을 컨트롤하는 빠른 방법

* `INCR`
  * 1 더한다
* `INCRBY`
  * n 만큼 더한다
* `INCRBYFLOAT`
  * float 값을 더한다
* `DECR`
  * 1 뺀다
* `DECRBY`
  * `n` 만큼 뺀다

### 이런 명령어들도 진짜 다 쓸까요?

* `INCR` 을 안쓰고 값을 업데이트 하려면?
  * `GET` 으로 갖고오고
  * 문자열을 숫자로 바꾼 후에
  * `SET` 으로 재설정한다.
  * 이 일련의 명령이 하나라도 실패하면 안됨!
  * 여러 API 서버 간 레디스를 공유해서 쓸텐데, 트랜잭션이 안 깨질려면?
  * 예시) 게시판의 게시글에 추천을 할 때, 동시에 여러사람이 추천을 하고, 그 중간값을 레디스에서 관리한다 가정하자. 어떻게 겹치는 문제를 해결할까?
    → 레디스는 근간이 싱글스레드임에 유의! 
    * 레디스 트랜잭션을 `WATCH` 명령으로 함께 처리
    * 락 걸기
    * `INCR` 쓰기

