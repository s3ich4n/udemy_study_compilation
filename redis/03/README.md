# 이-커머스 앱 셋업

## 첫 번째 할 일

1. 노드 깔아서 `rbay.zip` 압축풀고 구동시키기
2. `.env` 에 변수 추가해두기

## 내용?

* 각 언어별 Redis 클라이언트 라이브러리가 Redis에 커맨드 날리는걸 알아서 해준다
  * 파이썬이라면?
    * [redis-py](https://github.com/redis/redis-py), [aioredis](https://github.com/aio-libs/aioredis-py) 등등이 있을것
  * 노드진영은?
    * [node-redis](https://github.com/redis/node-redis)
  * 코틀린진영은?
    * Jedis
    * [lettuce](https://github.com/lettuce-io/lettuce-core)
  * 이런 라이브러리들은 보면 ORM처럼, 대충 쓸 수 있게끔 쉽게 만들어져있다
  * 그렇지만, 문서가 없는 경우도 있고 제대로 쓰기 위해선 [공식문서](https://redis.io/commands/)를 보며 커맨드를 제대로 이해할 필요가 있다

## 설치를 끝냈다면

구성된 환경은 아래와 같은 도식을 가진다.

![001-architecture-using-sveltekit](.\media\03_001.jpg)

* 요청을 날리면...
* SvelteKit을 통해 서버 사이드에서 렌더링된 페이지를 준다
  * 여기에 캐시 레이어가 추가된다! (Redis를 쓴다는 말)

## Redis와 SQL 각각에 쓰이는 방법론

### DB

- 데이터를 테이블에 넣고
- 어떻게 쿼리할지 구상한다

### Redis

* 어떤 쿼리에 값을 응답해야하는지 구상한다
* 해당 쿼리에 대해 "최고의" 해답이 무엇인지 구성한다

DB 방법론과 정반대다! 서로 상호보완한다고 생각하자!

### 지금은 어떤식의 접근을 하는지 살펴봅시다

1. 어떤 데이터를 저장할것인가? → 문자열 (아마도 렌더된 HTML 내용?)
2. 데이터의 크기를 고려해야할까? → 캐시되면 좋은(자주 변하지 않는) 페이지를 캐시하는게 이득일것이다
3. 데이터 만료가 필요할까? → 영영 캐시가 저장되어버리면 안되기 때문에 "적절한" 값을 운영하면서 혹은 적당값을 서비스에 맞게 저장해야한다.
4. 이런 데이터에 대한 키 정책은 어떤 것이 되어야 하나? → 후에 다룹니다
5. 다른 비즈니스 로직과 연관있나? → 그닥..

## 키 정책 방법론

### 키값으로 쓰려면?

1. 키값은 유일해야한다.
2. 다른 동료들이 키값만 보고 어떤 값이 있을지 이해할 수 있어야 한다.
3. 함수를 사용하여 키 이름을 생성하라 → 오타를 만들지 말라는 뜻. **휴먼에러 방지**!!!!!
4. `:` 을 이용해서 키의 depth를 사용할 수도 있다. 일종의 depth에 대한 delimiter 라고 보면 될 듯하다.
   1. 해당 강좌에서는 두가지 delimiter를 사용한다.
      1. depth 표현에는 `:` 를 사용
      2. 키 뒤에 유일무이한 값을 부여할 때는 `#` 를 붙여서 뒤에 입력
      3. E.g.,
         * `users#45`
         * `items#19`
         * `users:posts#901`
         * `posts#sdfglkn2134sdv`

## 코드를 건들여봅시다!

렌더되는 페이지로 예시를 들어보자

1. `pagecache#/about` → HTML 문서
2. `pagecache#/privacy` → HTML 문서
3. `pagecache#/auth/signin` → HTML 문서
4. `pagecache#/auth/signup` → HTML 문서

### `getCachedPage` 의 경우

1. 페이지 접근
2. 캐시되어있는지 확인
   1. 캐시값이 있으면 해당 값을 리턴
   2. 없으면 `null`을 리턴

### `setCachedPage` 의 경우

1. 캐시하고자 하는 페이지가 목록에 있는지 확인
2. 페이지를 캐싱하고 레디스에 저장