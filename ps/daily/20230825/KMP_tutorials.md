# KMP를 이해해보자

KMP(Knuth, Morris, Pratt) 알고리즘은 찾고자 하는 문자열(Pattern)을 주어진 문자열(Text)에서 빠르게 찾아내는 방법 중 하나

## Degenerate pattern?
- 패턴 속의 작은 패턴이 한 번 이상 반복되는 것을 의미

E.g., 
- `ABABAB`
- 여기 내에선 `AB`가 반복되는 중임

## Pi array 혹은 LPS(Longest proper prefix which is suffix)?

- prefix: 어느 문자열의 맨 앞부터 한 글자씩 추가시킨 값들의 리스트
- suffix: 어느 문자열의 맨 뒤부터 한 글자씩 추가시킨 값들의 리스트

E.g., `ABX` 라는 문자열에 대해:
- prefix: `A`, `AB` (A 기준, 0, 0-1)
- suffix: `X`, `BX` (X 기준, 2, 1-2)

E.g., `ABXAB`에서는?
- prefix: `A`, `AB`, `ABX`, `ABXA` (앞에서 ++1로 늘려감, 0, 0-1, 0-2, 0-3)
- suffix: `B`, `AB`, `XAB`, `BXAB` (뒤에서 --1로 늘려감, 4, 3-4, 2-4, 1-4)

LPS란?
- prefix와 suffix가 같을 때, 가장 길이가 긴 경우.
- 이 때, 이 쌍을 경계(_border_)라고 부른다.
- `lps[0]` 은 항상 0 이다.

## LPS에 대한 예시

pat = `"ABXAB"` 일 때, prefix, suffix를 구하며 LPS를 구해보자.

### 과정 설명

|index|substring|lps[index]|설명|
|-----|---------|----------|----|
|0|A|0|prefix, suffix가 "없음"<br />(1개짜리는 같지 않으니까 무시)|
|1|AB|0|prefix, suffix가 "일치하지 않음"<br />(2개짜리는 같은데 일치하지 않음)|
|2|ABX|0|prefix, suffix가 "일치하지 않음"<br />(2개짜리는 같은데 일치하지 않음)|
|3|ABXA|1|prefix, suffix가 일치하는 값은 "A", 길이는 1<br />(아! 이 안에서도 위의 prefix, suffix 연산을 하고 그 결과를 처리하는거구나!)|
|4|ABXAB|2|prefix, suffix가 일치하는 값은 "AB", 길이는 2<br />|

## LPS 구하기 - 코드

코드를 살펴봅시다.

### 보강 설명

- `lps[3]`, `lps[4]` 값에 주목하자.
    - `lps[3]=1`이라는 것의 의미는 `1` 길이의 Prefix와 Suffix가 동일하다는 것을 의미한다. (`ABXA` 라는 substring에 대해, prefix `A` == suffix `A` 이므로)
    - `lps[4]`?

## KMP Search

- 핵심
    - 패턴의 일부와 같다는 것을 알고있는 부분은 **스킵한다**.
    - 항상 두 개의 문자에만 접근해서 비교한다

1. 각 문자열의 인덱스 0부터 비교시작
    1. 패턴 검출 및 LPS 배열의 값 후의 내용을 확인

# 풀어보자

- 실전 예제 (1) - 염기서열에서 처리하기
- 실전 예제 (2) - [이 문제](https://leetcode.com/problems/longest-happy-prefix/description/) 풀기

# References

제가 이해할 수 있게끔 좋은 게시글을 올려주셔서 감사합니다!

- [[Python] KMP 알고리즘으로 문자열 찾기](https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/)
- [String Algorithms, CS 97SI (Stanford University)](https://web.stanford.edu/class/cs97si/10-string-algorithms.pdf)