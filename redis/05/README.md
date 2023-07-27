# 해시를 살펴봅시다

레디스에서는, 키값을 받고 k/v 쌍을 반환하는 것을 해시라고 한다.

* nested된 정보는 담을 수 없다!
* json의 array도 담을 수 없다!

## 해시 명령을 살펴봅시다

### 해시값 저장

```sql
HSET company name 'Concrete Co' age 1915
>>> 2
```

`company` 는 해시를 참조하는 키. 나머지는 필드/밸류/필드/밸류/.... 를 반복

### 해시값 읽어오기

```shell
HGET company name
```

`HGET` 명령어는 키, 필드 순으로 입력해주어야 한다.

### 해시값 전부 가져오기

```shell
HGETALL company
>>> raw return value...
["name","Concrete Co","age","1915"]
```

래핑된 라이브러리들은 알아서 언어에 맞게 파싱해준다는 사실을 기억하기.

### 해시값 존재하는지 확인

```shell
HEXISTS company age
>>> 1
HEXISTS company asdkjnaesrfd
>>> 0
```

### "전체" 해시값 삭제하기

```shell
DEL company
>>> 1
```

### 해시 키/밸류 일부 삭제하기

```shell
HDEL company age
>>> 1
```

### 해시 내의 숫자(정수/부동소수) 값 +1 하기

```shell
HINCRBY company revenue 10
>>> "10" (키가 없으면 새로 생성한다.)
HINCRBYFLOAT company age 1.004
>>> "1.004"
```

### 해시 내 문자열의 길이 구하기

```shell
HSTRLEN company name
>>> "10"
```

### 해시 내 모든 키 구하기

```shell
HKEYS company
>>> [
  "name",
  "revenue",
  "age"
]
```

### 해시 내 모든 밸류 구하기

```shell
HVALS company
>>> [
  "Concrete Co",
  "40",
  "2.002"
]
```

