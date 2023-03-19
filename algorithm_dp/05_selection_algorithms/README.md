# Selection Algorithms

## 들어가기에 앞서

- 해당 문서 참조
  - [선택 알고리즘](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
- 여기서는 quickselect와 median of medians를 다룸

### 선택 알고리즘

- k번째로 작은/큰 값을 자료구조내에서 찾기위한 알고리즘을 의미
- 최대값/최소값/중간값을 찾는 것이 목표
- O(n) 정도의 선형 시간복잡도가 목표
- quickselect 혹은 median of medians 같은 알고리즘이 있음

### 정렬을 하면?

- 정렬된 배열에선 k번째 값을 k-1번째 인덱스로 가져올 수 있다
- 단독 아이템을 가져올 때는 불필요한 어프로치다.
- 정렬은 O(N log N)이 가장 최선의 케이스다
- k번째 [order statistic](https://ko.wikipedia.org/wiki/%EC%88%9C%EC%84%9C%ED%86%B5%EA%B3%84%EB%9F%89)을 구하는데 효율적인 접근법이다.
- 선택 알고리즘은 정렬 접근법으로 축소될 수 있다(selection can be reduced to sorting approaches)

### 적절한 자료구조를 사용하면?

- 균형 이진트리, 힙을 사용하는 방안이 있겠음
- 추가 메모리를 사용해야 하지만, O(log N) 정도로 실행속도를 줄일 수 있음
- 선택 알고리즘은 [in-place](https://www.geeksforgeeks.org/in-place-algorithm/)임. 다시말해 추가 메모리가 필요하지 않음을 의미.

### online selection 문제

- [online algorithms](https://en.wikipedia.org/wiki/Online_algorithm)은 입력값을 전체 입력을 받을 수 없는 상황에서 순서대로 처리하는 방식이다.
- 다시말해, 전체 입력값이 무엇인지 모름을 의미한다.
  - 예시) 데이터 다운로드를 유지해야되고, k번째 순서를 알고싶은 경우
- 미리 값을 알고있지도 않다.
- 가능성을 두고 이게 그거인갑다 하는 "근거있는 추측"은 할 수 있다.
- 이를 [secretary problem](https://en.wikipedia.org/wiki/Secretary_problem)이라 부른다.

## Quickselect 알고리즘

### 소개

- [Quickselect 알고리즘](https://en.wikipedia.org/wiki/Quickselect)은 선택 알고리즘이다.
- 정렬되지 않은 배열에서 k번째 값을 찾을 수 있다.
- 최악의 경우 O(N^2) 만큼, 최적의 경우에는 O(N) 만큼의 시간복잡도를 가진다.
  - 최악의 경우 예시: 정렬된 배열의 가장 큰 값을 찾는 경우
- in-place 접근법이다. 다시말해 메모리 추가 사용을 일절 하지 않는다는 점이다. (최고장점)

### 소개 cont'd

- quicksort와 매우 유사하다
- 양쪽 배열 끝을 재귀연산 했던 것과는 다르게, 한쪽을 quickselect를 수행한다.
- 알고리즘 간단 소개
  1. 랜덤하게 피벗 아이템을 선택한다(방법은 사실 다양함).
  2. 피벗 아이템을 기반으로 배열을 파티션으로 나눈다
  3. 한쪽 부분만을 사용한다.

### 알고리즘 상세설명 1부: 파티션

- 피벗에 근거하여 배열을 파티셔닝하는 단계
  - 피벗을 랜덤하게 선택(첫번째 인덱스부터 마지막 인덱스 사이의 값을 하나 고름)
    - 이 때, 중간값을 뽑아도 된다만, 랜덤값이 보다 나은 어프로치다.
  - 배열을 재배치한다(정렬이 아님!)
    - 피벗보다 작은 값은 왼쪽, 그보다 큰 값은 오른쪽
    - 이때는 피벗값에 해당하는 인덱스가 리턴된다
- 배열을 반 나누는것이 핵심이다.
  - 왼쪽(좌측 서브배열)
    - 작은 값을 찾을 때
    - n 번째로 작은 값을 찾을 때 (3번째로 작은 값)
  - 오른쪽(우측 서브배열)
    - 큰값을 찾을 때
    - n 번째로 큰 값을 찾을 때 (2번째로 큰값)

### 알고리즘 상세설명 2부: 선택

- 파티셔닝이 끝나면 3가지 케이스가 있음
  1. k가 피벗과 같으면?
     - k번째 작은/큰 값을 찾은 것을 의미.
     - 파티셔닝이 필요한 이유: k-1개의 아이템이 피벗보다 작은 값만큼 있기 때문
  2. k가 피벗보다 작으면?
     - k번째 작은값은 좌측 서브배열에 있다.
     - 우측 서브배열을 버림
  3. k가 피벗보다 크면?
     - k번째 작은값은 우측 서브배열에 있다.
     - 좌측 서브배열을 버림

## 피벗 선택의 문제?

- quickselect 알고리즘은 피벗 선택에 대해 성능이 민감하게 변한다.
- 매 파티션은 O(n)의 선형 실행시간을 가진다.
- 아이템을 잘 솎아내지 못하면, O(n^2) 까지 실행시간이 늘어난다(!)
  - 예를들어..
    - 가장 작은 값을 고른다고 했을 때
    - 가장 큰 아이템을 매 반복마다 피벗으로 골랐을 때이다.
    - O(n) 연산을 N번 반복하는 꼴이되고 만다.
- 우측 피벗을 잘 고르려면?
  - 중앙값([median](https://ko.wikipedia.org/wiki/%EC%A4%91%EC%95%99%EA%B0%92)을 의미, 이하 중앙값 사용)을 고르면 O(n) 정도의 선형 수행시간을 얻을 수 있다.
  - 그러면 좌/우측 서브 배열의 값이 같을 것이다.
    - quickselect 로직을 사용하되 중앙값을 피벗으로 하여 정렬하는게 median of medians 알고리즘이다.
  - 추가 메모리 소모가 있을 수 있는데, 사용량은 O(log N)이다.

## median of medians?

- 중앙값을 고르고, 이를 피벗으로 쓰는 것 말곤 quickselect 의 방법과 같다.
- 작은 배열을 정렬하는건 O(N) 정도의 선형 시간을 가진다 - insertion sort 같은 것들...
- 중앙값은 아래 로직으로 찾는다.
  - 기존 배열을 `5`개 값을 가진 청크로 나누고 이를 정렬한다.
    - 왜 `5`개 인가?
      - 청크가 너무 작지도/크지도 않게 나눠지도록 하기 위함
      - 재귀호출을 너무 많이 하지 않도록 하기 위함
  - 나눈 배열의 중앙값을 정순으로 정렬한 값이 **중앙값** 이다.
- 찾은 중앙값을 토대로 중앙값들의 중앙값을 계산한다.

### 알고리즘 분석

- 중앙값들의 중앙값 구하기
  - 청크단위로 나눈 배열들의 중앙값들을 구하고, 배열들을 정렬한다 (O(N) 만에)
  - 그 값들의 중앙값들을 모두 구해서, 그 중의 중앙값을 구한다.
    - median of medians를 구함
    - 해당 값을 구하고, median of medians 값과 배열 중앙값의 인덱스의 값을 스왑함
- 선택정렬을 하기에 딱 좋은 중앙값이 게산되었음

## Introselect 알고리즘

- quickselect는 메모리 절약차원에서 효과가 좋지만, 피벗을 잘못 고르면 느려진다
- median of medians는 O(N)의 속도를 보장하지만, 메모리를 더 쓴다.
- introselect는 두 장점을 적당히 합쳤다.
  - quickselect로 시작해서 진행이 너무 느리다싶으면 median of medians를 수행한다.

## Secretary problem

- [해당링크](https://en.wikipedia.org/wiki/Secretary_problem)를 먼저 읽고 오십시오
- 그간 k번째 순서 통계량([order statistic](https://en.wikipedia.org/wiki/Order_statistic))을 살펴봤다.
- 그러나 k번째 순서 통게량 일련의 값(order statistics of a stream)을 찾으려면?
  - 예를들어...
    - 웹에서 데이터를 다운로드 받는 경우
- 그것이 online algorithm이다. 처음부터 전체 입력을 사용할 수 없는 상태에서 데이터를 처리해야한다는 것을 의미한다.
  - 전체 데이터가 없으니 파티션 기반의 접근법을 사용할 수 없다.
  - 이 문제는 파티션 기반의 접근법을 사용하지 않는다.
  - 문제는 (이러한 제약 조건 하에서) 최대 확률로 입력 데이터 시퀀스의 특정 요소를 선택하는 것이다.

## Secretary problem (cont'd)

- [Secretary problem](https://en.wikipedia.org/wiki/Secretary_problem)은 [최적의 멈춤 이론](https://en.wikipedia.org/wiki/Optimal_stopping)의 가장 중요한 부분이다. 이는 best choice problem 이라고도 불린다.
  - [이 게시글](https://johngrib.github.io/wiki/secretary-problem/)도 다시 읽어볼 것
- secretary problem 설명
  - N명의 후보자 중 최고의 비서를 뽑는 문제다
  - 면접대상자는 한명씩만 면접보고, 거른 면접대상자는 다시 부르지 못한다.
  - 전체 면접대상자에 대해 순위는 매길 수 있지만, 아직 못만나본 후보는 판단할 수 없다.
  - 그런데 결정을 당장 해야한다! → 이러면 quickselect를 사용할 수 없다!
  - 이 때의 최적의 전략은 뭘까?
- secretary problem: 최적의 전략
  - n/e (단, e는 자연로그, euler's number라고 한다)의 후보를 탈락시키고, 그간 인터뷰한 후보 중 가장 나은 후보를 뽑는 것이다.
  - 이는 1/e stopping rule 이라고도 한다. 최고의 후보를 뽑는 확률이 대략 37% 가량이기 때문이다.
  - 이 알고리즘은 [Odds Algorithm](https://en.wikipedia.org/wiki/Odds_algorithm)에서 따왔다.
  - 사용하면서 Keith order statistics를 사용할 수도 있다.
  - optimal solution은 적절한 트레이드오프를 가져야한다. 너무많은/너무적은 값들 중 값을 찾으면 제대로된 판단을 할 수 없다
