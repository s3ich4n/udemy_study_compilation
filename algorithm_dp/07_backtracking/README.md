# 백트래킹

- 브루트포스?

  - 하것냐

- 백트래킹?
  - 한번의 반복으로 여러 배드케이스를 거른다
  - 후보 A가 문제 해결에 적합한 후보가 아니라면 A를 해결책으로 두지 않는다.
  - 이런 형태의 문제를 "트리구조"로 푼다. 그래서 game tree, potential search tree라고 부른다
  - 각각의 부분 후보들은 개별인 추가과정이 다른 후보들의 부모다.
  - 각 트리의 끝은 더 확장되지 않는 개별 후보다.
  - 백트래킹 알고리즘은 트리를 재귀적으로, 루트에서부터 타고내려가는 순회과정이다.
  - 그래서 트리에 구현되면 depth-first search라고 불린다.
- depth-first search?
  1. 알고리즘은 모든 노드에 대해 주어진 노드가 적합한 해결책으로 풀리는지 점검한다.
  1. 만약 해결하지 못하면 그 아래 서브트리는 무시된다(이게 백트래킹의 주요 장점)
  1. 모든 노드의 서브트리를 재귀적으로 센다.
- 백트래킹 cont'd
  - 백트래킹은 재귀의 형태다
  - 모든 문제에 대해 몇몇 computational problem 으로 해결하기 쉬운 일반적인 알고리즘
  - 이런 문제는 constraint sastifaction problem이라고 부른다.
  - 백트래킹은 Combinatorial optimization problem(순회 판매원 문제 등)을 푸는데도 중요하다
  - 이따금씩 모든 케이스에 대해 일일이 연산하는 것 보단
  - n-queens 문제나 스도쿠 풀이가 대표적이다

## 쫓아가봅시다

depth-first?

- 보고있는 가지가 답이없으면 아래 가지를 모두 포기한다
- 아래 가지는 현재 가지를 기반으로 뻗어나가는 것으로 간주하기 때문

# 1. N-Queens 문제

- N개의 "퀸"을 NxN 체스보드에 두는 문제 -> 두 퀀이 서로 위협하지 못하는위치를 찾으라
- 퀸은 가로세로대각선 모두 갈 수 있다.
- 원래 문제는 N=8일때를 가정했다.
- structured programming의 위력을 보여준다.

- 가능한 경우의 수는? O(n^n) - brute-force 하면 O(n!) 만큼의 수행시간이 든다는 뜻....
  - 세야할 케이스가 너무 많다!
- 불가능한 수를 모두 쳐내면 O(2^n) 만큼은 쳐낼 수 있다... 그래도 느리긴 느리다!

## 살펴봅시다

N-queen 문제를 트리로 생각하면...

1. 1번째 값을 둔다
   1. 자식을 만들고 또 타고들어간다
   1. 답이 안맞겠다 싶으면 현재 단계부터 모든 자식을 포기한다.
      1. 벌써부터 답이 아니므로
   1. 다시 이전단계로 돌아가서 찾아본다

근데 앞서말했듯 이건 NP-complete이기 때문에 100을 넣으면 터진다

## 해설을 들어보자

### 어프로치

안되는 경로는 바로 자기자신을 포함해서 포기하는게 핵심이다.
어떻게 쫓아갈지를 확실히 알고있다

# 2. 해밀토니안 사이클 문제

- G(V, E) 그래프는 V개의 노드(vertices)와 E개의 링크(edges)를 갖고있다
- 해밀턴 경로는 방향이 모든 간선에 딱 한번씩 방문하는 경로가 있는, 방향이 있는/없는 그래프
- 해밀턴 사이클은 해밀턴 경로 중 사이클이 있는 것을 의미한다
  - 브루트포스 하면 O(N!) 시간복잡도에 푼다.
  - 백트래킹을 하면 하나의 이터레이션에 풀수있다
- G(V, E) 그래프에는 해밀턴 경로가 몇개 있을 수 있다

## 살펴봅시다

방향없는 그래프를 2x2 배열로 풀어보자

- 해밀턴 사이클 문제 cont'd
  - 해밀턴 문제는 경로/사이클이 G(V, E) 그래프인지 아닌지 판단하는 문제다.
  - 이 문제는 NP-complete이다.
  - dirac-principle
    - G(V, E) 그래프
    - V개의 점을 가지고있는데, 모든 점의 차수가 V/2 보다 크거나 같은 경우
  - 차수는 점의 경로의 수를 의미함
  - 해밀턴 경로를 찾는건 NP-complete 이지만 어떤 경로가 선형 시간내에 topological order를 따르는지 아닌지 분간할 수는 있다.

# 2. 해밀토니안 사이클 문제 cont'd

백트래킹 알고리즘

1. 랜덤노드로 시작한다(인덱스 0 같은..)
2. 현재 노드에 이웃을 게속해서 추가한다. 해결책 리스트에 들어가지 않았는지 확인해야한다
3. 되돌아갈 수 있어야한다

## 해설을 들어보자

바로 쫓아갈 수 없는 경로는 쳐낸다.

이런 그래프가 있다 치자...

```
A - B
|   |
C - D
```

### 쫓아가기 2-1

```
    B


```

### 쫓아가기 2-2

가능하다.

```
A - B


```

불가능하다! 이런 캐이스는 그 아래로는 전부 쳐낸다-> 그래프로 이을 수가 없기때문

```
   B

C
```

# 3. Coloring Problem

[이 문제](https://en.wikipedia.org/wiki/Graph_coloring)에 대해 다룬다.

- 1페이지
  - G(V, E) 그래프의 노드들에 색칠을 해야된다. 두 인접한 노드는 동일한 색을 가지면 안된다.
  - 주어진 색상은 정수다
  - G(V, E)에 필요한 최소한의 색의 갯수는 chromatic number라고 부른다.
  - 하나 이상의 해답이 있을 수 있다.
  - E.g., 4개의 간선에 대해서는 3가지 방법으로 12개의 방법이 있을 수 있다.
- 2페이지
  - 이 문제 또한 NP-complete 이다.
  - 가능성이 지수함수적으로 늘어나있다.
  - k개의 색깔을 G(V, E) 그래프에 칠하고자 한다면 실행시간은 `O(k^v)` 이다.
  - 브루트포스 하면 의미없다는 말

## Coloring problem 응용 (1)

Bipartite graph (이분 그래프, [참고링크](https://en.wikipedia.org/wiki/Bipartite_graph))

- 그래프가 `2`가지 색으로 그러야하는지 결정하는 것은 그래프가 bipartite(이분) 한지 결정하는 것과 같다.
- 이 문제는 BFS로 O(N) 에 해결할 수 있다
- 모든 꼭짓점을 빨강과 파랑으로 색칠하되, 모든 변이 빨강과 파랑 꼭짓점을 포함하도록 색칠할 수 있는 그래프이다.

## Coloring problem 응용 (2)

스케줄링

- 대학의 시험문제를 만드는 것이 목적인 경우
- 여러 과목과 여러 과목을 수강하는 여러 학생들이 있다. - 많은 과목은 동일한 학생 수를 가진다
- 어떻게 하면 두 과목을 수강하는 학생들의 시험시간이 겹치지 않도록 시험일정을 작성할 수 있을까?
- 모든 시험을 스케줄링하는데 필요한 최소한의 타임 슬롯이 얼마일까?
- 이 문제 또한 G(V, E) 그래프로 표현할 수 있다. 이 때 모든 노드는 과목이고, 두 노드 사이의 간선들은 학생이다.
- 즉 G(V, E) 그래프의 coloring problem이다. 이는 타임슬롯의 최소 수는 그래프의 k chromatic number이다.

## Coloring problem 응용 (3)

라디오 주파수 할당

- 라디오 탑에 주파수가 할당되면 동일 위치의 타워에 할당된 주파수는 반드시 달라야한다. 전파간섭을 피하기 위함이다.
- 어떻게 전파간섭 없이 주파수를 할당할 수 있을까? 최소한의 주파수 수는 몇일까?
- 이 문제 또한 graph coloring 문제이다. 이 때 모든 라디오 탑은 노드를 의미한다.
- 두 라디오 탑 사이의 간선은 각자 범위안에 있음을 의미한다.

## Coloring problem 응용 (4)

레지스터 할당(PC)

- 컴파일러 최적화는 coloring problem과 매우 연관이 깊다.
- 레지스터 할당은 많은 수의 타겟 프로그램 변수를 작은 cpu 레지스터에 할당하는 과정이다.

## Coloring problem 응용 (5)

지도 색칠

- 국가/주가 그려진 지도를 색칠하는데, 인접한 국가 혹은 주에서는 동일한 색을 사용하지 않기 위한 경우가 있다.
- 이게 널리 알려진 알고리즘 문제다.
- 어떤 지도든 4가지 색깔로 처리가능하다. 그런고로 four color theorem이라고 부른다.

## Coloring problem 해결 알고리즘

1. greedy approach - 답을 찾을 수는 있지만, 최적의 답은 아니다(색상을 더 사용할 수 있음)
1. backtracking - 한번의 iteration 내에 bad state를 무시/제거할 수 있다. (혹은 재귀호출)
1. Powell-Welsh 알고리즘 - 노드를 차수(간선의 수)에 근거하여 정렬한 결과에 달려있다.

## Coloring problem (cont'd)

- "색상"을 각자 다른 노드들을 색상으로 두며, 이를 (index `0`으로 시작하는) 최초의 노드로 두자.
- 색상을 부여하기 전, 이미 인접한 노드에 유사한 색상이 있는지 점검해야한다.
- 적절한 색상을 찾으면, 그 부분의 해답으로 색상을 칠한다.
- '충돌'로 색상을 못찾으면 **백트래킹** 한다.

# Coloring problem - 시각화

- 트리로 접근한다.
  - vertex 0 을 최초 노드로 두자.
  - 그 자식으로 발생할 수 있는 vertex가 계속해서 생기겠지...
  - 일어날 수 없는 케이스면 바로 **백트래킹** 한다. 이게 속도 향상의 핵심!

# Coloring problem - 구현

코드 참고

# Knight's Tour Problem

- 소개
  - 문제: 모든 N\*N 체스판 내의 모든 셀에 '딱 한번'만 방문하고 싶은 경우를 의미.
  - closed tour - knight의 마지막 지점은 시작지점과 항상 동일하다.
  - Kinght's tour problem은 해밀턴 경로 문제의 보다 정형화된 형식이다.
  - 그렇다면 이 문제 또한 G(V, E) 그래프의 해밀턴 경로를 찾는 문제다.
- 문제사항
  - 탐색하는 공간의 크기는?
  - Kinght는 한번의 iteration 내에 여덟 번 움직일 수 있다. 그렇지만 N\*N배열에 서 해야한다.
  - O(2^3*(N*N)) 만큼의 시간 복잡도를 가진다
  - 해밀턴 경로와는 다르게 divide-and-conquer 기법을 통하여 O(N) 만에 해결가능하다.
- M\*N 체스보드에서는 항상 가능하다. 아래 조건이 아니면...
  - M, N 모두 홀수가 아닌 경우
  - M=1, 2, 4인 경우
  - M=3, N=4, 6, 8인경우

# Kinght's Tour Problem

- x, y축 움직임을 배열로 빼둔다.
- 8\*8 돌리는데 꽤 걸린다 (1분 안이긴 한데 타임아웃 날거임)

# Maze Problem

- N\*N 미로를 나가는 알고리즘을 만들어보자.
- N\*N 배열을 다시 생각해보자.
- 가장 효율적으로 나가는 방법은? (자동청소기 같은...)
- 백트래킹? 혹은 **Depth-first search**

# Maze Problem (cont'd)

이런 문제를 풀기 위한 알고리즘은 여러가지가 있다

1. 미로를 알고있다면

- heavy-weight graph 알고리즘을 쓴다
  - 다익스트라 알고리즘
  - A\* 검색

1. 미로를 모른다면?

- 백트래킹을 사용한다
  - Trémaux 알고리즘 혹은 depth-first search

# Maze problem (구현)

이해를 위해 반드시 돌려볼것

1. 2차원 배열을 구현

- 전체 미로의 크기
- `0`은 못가는 곳(장애물)
- `1`은 갈 수 있는 곳

2. 움직임을 구현

- 상/하/좌/우

# 스도쿠

- 소개
  - 3\*3 배열 9개가 있는 9\*9 배열
    - 3\*3 배열에는 1~9가 하나씩 존재
    - 9\*9 배열에는 행당 1~9가 하나씩 존재
  - 유일한 해결책이 존재하는 부분적으로 완벽한 격자
- 살펴보기
  - NP-complete 문제다. 브루트포스를 하면 `O(M^N)` 만에 풀린다는 말
  - M은 개별 셀에 들어갈 수 있는 경우의 수를 의미하고, N은 채워야할 빈 필드를 의미한다.
  - 백트래킹을 사용해보자.
  - 특정 지점마다 1~9부터 넣어보고, 아니다 싶은 가지를 prune.

# 백트래킹의 문제점?

- n-queen 문제서 O(n!) 지수적 러닝타임을 감소시켜봤다
- coloring problem도 마찬가지였다.
- NP-complete, NP-hard 문제는 가능성이 많기 때문에 그렇다.

# 백트래킹의 문제점 - 해결책

- 메타-휴리스틱을 사용한다. -> 근사치를 구하자
  - genetic algorithms
  - simulated annealing
  - colony optimization
