# Redis란?

## 들어가기에 앞서

이 강의는 Redis 7.x 기반이다.

## Redis란?

DB다.

Redis(이하 레디스)는 빠르다. 이유는...

1. 관련 정보를 메모리에 담는다
   1. 그렇다고 많은걸 다 담을 수는 없지만, 그에 대응하는 적절한 운영/개발 전략이 있다
2. 데이터가 간단한 데이터 구조로 담겨있다
   1. Doubly linked list
   2. Sorted set
   3. Hash map
3. 간단한 피처 셋(Feature set)을 갖고있다
   1. 전통적인 RDBMS에 대비하여 데이터 스키마, FK 제한, SQL등등의 제한이 크게 없다

한정된 메모리와 간단한 구조로 어떻게 데이터를 잘 담아둘 것인지를 고려하는게 레디스 사용의 핵심이다.

## 무료 레디스 클라우드 사용방안

- 시작

  1.  redis.com 에 회원가입 후 프리티어 사용
  1.  DB 생성 (프리티어로 만들기)
  1.  이름만 정해주고 create
  1.  DB 선택 후 Public endpoint와 Default user password를 [rbook.cloud](http://rbook.cloud) 에 입력하기

- 이후

  - [https://rbook.cloud/](https://rbook.cloud/) 여기에서 에제를 입력하거나, 내 로컬에서 띄우거나.
