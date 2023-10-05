## Follow-up 내용이 시사하는 바는?

> Could you solve the problem in linear time and in O(1) space?

와 이게 되나?

## Boyer-Moore majority vote algorithm

어떤 배열에서 과반수인 값을 $O(n)$ 의 시간에 $O(1)$ 만의 공간복잡도를 이용하여 찾을 수 있다.

로컬 변수에 시퀀스 요소와 카운터를 유지하며 카운터는 처음에 0으로 유지.
시퀀스의 요소를 한 번에 하나씩 처리.
    요소 x를 처리할 때 카운터가 0이면 알고리즘은 x를 기억된 시퀀스 요소로 저장하고 카운터를 1로 설정합니다.
    그렇지 않으면 x를 저장된 요소와 비교하여 둘이 같으면 카운터를 증가시키거나 그렇지 않으면 카운터를 감소시킵니다.
이 프로세스가 끝날 때 시퀀스가 과반수를 차지하면 알고리즘에 의해 저장된 요소가 됩니다. 이는 의사 코드로 다음 단계로 표현 가능:

### 의사코드

1. 요소 m과 카운터 i를 i = 0으로 초기화합니다.
2. 입력 시퀀스의 각 요소 x에 대해:
    1. i = 0이면 m = x, i = 1을 할당합니다.
    2. 그렇지 않으면 m = x이면 i = i + 1을 할당합니다.
    3. 그렇지 않으면 i = i - 1을 할당합니다.
3. m을 리턴.

### 쉽게 좀 풀어봅시다

말이 좀 길었는데, 쉽게 설명하면 아래와 같다[^1]:

> 하나의 성을 차지하기 위해 여러 나라가 전투를 벌인다. 여러 나라에서 온 병사들은 일렬로 줄을 서 있고, 한 명씩 차례대로 성을 향해서 돌진한다.
>
> 만약 성에 아무도 없다면 바로 성을 함락하여 성의 주인이 된다. 성에 누군가가 있다면 2가지 케이스로 나뉜다.
>
> 성에 있는 사람이 나와 같은 나라 사람이면 성에 합류하고, 다른 나라 사람이면 싸워서 성에 있는 병사 한 명과 동반 자살(?)한다.
>
> 즉, 성에 있는 사람 수를 1만큼 감소시키는 동시에 자기 자신 또한 사라진다.
>
> 어떤 나라가 성을 함락하는 순간 다른 모든 나라는 같은 팀이나 다름없다. 왜냐하면 모두 성을 향해서만 공격하기 때문에 성을 함락한 나라의 병사 숫자가 집중적으로 감소하기 때문이다.
>
> 모든 병사가 돌진한 뒤에도 성에 병사가 남아있다면 그 병사의 나라가 최종적으로 성의 주인이 된다. 만약 성에 아무도 남지 않는다면 마지막으로 성을 소유했던 나라가 성의 주인이 된다.

### 로직

```python
from typing import List

def majorityElement(nums: List[int]) -> List[int]:
    """
    이러면 "가장 최고빈도의 값"을 갖고오는 셈이다.

    MAJORITY 알고리즘의 구현체.
    """
    majority = counter = 0

    for number in nums:
        # 성의 주인을 바꾸는 로직
        if counter == 0:
            majority = number
            counter = 1
        # 성을 함락한 적이 있다면?
        elif majority == number:
            counter += 1
        # 동반자살 로직
        else:
            counter -= 1

    # "과반수"인 값을 리턴
    return majority


print(majorityElement(nums=[[2,3,1,1,4,4,4,4,4,4,4,4,4,4,2,2,2,2,21,1,3]))
>>> 4
```

### (내 기준) Pitfalls

1. 과반수가 아니라 딱 절반일 때는 적용할 수 없더라!

```python
print(majorityElement(nums=[1, 1, 1, 2, 3, 3]))
# 주어진 배열이 [1, 1, 1, 2, 3, 3] 이라면 결과값이 1이 되지만, 
>>> 1
print(majorityElement(nums=[2, 1, 1, 3, 3, 1]))
# 같은 구성에 순서만 바꾼 [2, 1, 1, 3, 3, 1] 이라면 결과값이 3이 된다.
>>> 3
```

2. 이 알고리즘을 _단독으로_ 구동하면, 과반수가 없어도 값을 리턴한다. 따라서 보정을 위해 두번째 과정(_second pass_)을 거쳐야한다!

## Misra-Gries heavy-hitters algorithm

`n`개의 요소를 가진 가방 `b`에서 $n / k$ 이상 나오는 값을 찾으라. 라는 문제로 주로 설명된다(딱 이번 문제).

이 동작으로 인해 k-reduced bag은 k개의 다른 값보다 적은 가방을 갖게된다.

Misra-Gries 알고리즘은 정리와, 그에 따른 1st pass, 2nd pass가 있다.

- 정리 1: 각 b의 heavy-hitter 는 b의 k-reduced bag의 엘리먼트이다.
    - 1st pass: k-reduced bag인 t를 만든다
    - 2nd pass: t의 엘러먼트를 heavy-hitter로 선언한다 (n/k times in b라면)

정리 1을 통해 이 프로시저는 heavy-hitter인 모든, 유일한 값을 결정한다.

t를 만들기 위해, b를 임의의 순서대로 스캔한다. 특이성을 위해 다음 알고리즘은 인덱스가 증가하는 순서로 스캔한다.

알고리즘의 불변량 P는 t가 스캔한 값에 대해 k-reduced bag이고, d는 t에 포함된 고유 값의 수이다. 처음에는 스캔한 값이 없고, t는 빈 가방이며, d는 0이다.

```
P: 0 ≤ i ≤ n ＾
    t is a k-reduced bag for b[0:i – 1] 
    d is the number of distinct values in t  0 ≤ d < k
```

요소 b[i]를 스캔할 때마다 불변성을 유지하기 위해 (1) b[i]가 t에 없으면 t에 추가하고 d를 1씩 증가시키고, (2) b[i]가 t에 있으면 t에 추가하지만 d는 수정하지 않고, (3) d가 k와 같아지면 t에서 고유 값 k를 삭제하여 t를 줄이고 d를 적절히 업데이트합니다.

t의 가능한 구현은 (vi, ci) 형식의 쌍 집합으로, 여기서 각 vi는 t의 고유 값이고 ci는 t에서 vi의 발생 횟수입니다. 그런 다음 d는 이 집합의 크기입니다. "t에서 고유 값 k개 삭제" 단계는 각 ci를 1씩 줄인 다음 ci가 0이 되면 집합에서 모든 쌍(vi, ci)을 제거하는 것과 같습니다.

t의 AVL 트리 구현을 사용하는 이 알고리즘의 실행 시간은 $O(n \log_{ } K)$ 입니다. 공간 요구 사항을 평가하기 위해 b의 요소에 가능한 값이 m 개일 수 있으므로 값 vi를 저장하는 데 O(log m) 비트가 필요하다고 가정합니다. 각 카운터 ci는 n만큼 높은 값을 가질 수 있으므로 저장소에는 O(log n) 비트가 필요합니다. 따라서 O(k) 값-카운터 쌍의 경우 필요한 공간은 O(k (로그 n + 로그 m))입니다.

### 뭔소리임?

$O(c \log_{ } m)$ 비트를 2번 루프돌려서 구할 수 있다는 뜻이다.

카운터 `c`값 이상을 포함하는지 확인하기 위해, 배열을 루프를 돌리자. 그 개별요소 x 값에 대해...

1. if
    - x값에 대한 카운터가 있다면, `카운터++`
2. elif
    - 카운터가 없지만 `c` 카운터보다 작다면, `x` 요소에 대한 카운터를 새로 만들고 `1`로 초기화
3. else
    - 그 외: 배열 `keys` 에 대해... 그 길이가 `c` 카운터보다 크면
    - 모든 카운터를 `1` 줄임. 카운터가 `0`인값은 **삭제**함.

결과: 카운터 `c` 값보다 많은 값들이 해시테이블(파이썬에선 딕셔너리)에 있다. 그 값들만 리턴.

## 참고링크

- 구현체가 있거나 직접적으로 도움 된 링크
    - https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
    - http://www.crm.umontreal.ca/pub/Rapports/3300-3399/3302.pdf
    - https://leetcode.com/problems/majority-element-ii/solutions/63520/boyer-moore-majority-vote-algorithm-and-my-elaboration/
- 개념 학습에 도움 된 링크
    - https://users.cs.utah.edu/~jeffp/teaching/cs5140-S16/cs5140/L11-Heavy-Hitters.pdf
    - https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary
    - https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_heavy_hitters_algorithm
    - https://people.csail.mit.edu/rrw/6.045-2019/encalgs-mg.pdf
    - https://www3.cs.stonybrook.edu/~rezaul/Spring-2013/CSE638/Streaming-Algorithms-(Ajinkya-and-Hemanga).pdf

[^1]: 출처: https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/#%EC%A6%9D%EB%AA%85
