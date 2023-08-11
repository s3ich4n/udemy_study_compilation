# 스택메모리, 힙메모리

스택 메모리는 함수 호출지, 로컬 변수를 저장하는 영역이다. 이게 있어서 어디서 참조하고 없애고 하는 것들이 가능하다. fragmentation이 없다.

힙 메모리에는 객체들이 생성되어 저장된다. 힙 메모리는 x86, x64에서 Executable에 대해 줄 수 있는 만큼 논리적으로 사용 가능하다. 함수 내에서 힙 메모리를 생성한 후에는, 함수 호출이 종료되어 더이상 해당 객체에 "참조" 하는 값이 없어지면, GC가 알아서 삭제한다.

# Recursion

문제를 점점 더 작은 문제(subtask)로 풀기 위한 어프로치다. 무한루프를 피하기 위해 사용되는 가장 좋은 접근법이다.

모든 문제는 Iteration, Recursion으로 풀 수 있다.

Recursion은 두 종류가 있다.

## Tail recursion

함수의 끝에서 재귀호출을 하면 tail recursion이라고 부른다. loop문과 유사하다. 다음 recursive call 전에 모든 구문을 수행한다.

## Head recursion

함수의 초반부에 재귀호출을 수행하면 head recursion이라고 부른다. 다음 recursive 호출 전, 함수 내 현재 "상태값(함수호출 현황, 지역변수)"을 저장할 수 있다. 다시말해, 메모리 사용량이 더 늘어날 수 있다는 점이다.

# Recusion과 스택 메모리

수행속도는 적어도 O(2N) 이다. 스택에 함수호출을 넣었다가 빼는 것 만으로도 일이다.

N 만큼의 팩토리얼값을 구하는 연산을 쓸 때도 상황은 마찬가지이다.

## Head recursion을 피해야하는 이유?

너무 많은 프레임을 사용하여 RecursionError 가 발생할 수 있다. 파이썬 오브젝트 호출에 사용되는 최대 depth가 1000 이하이기도 하다. 그런 이유로 어지간하면 재귀 구현 시 Tail recursion으로 호출하기를 권장한다.

또한 재귀함수를 사용할 때의 값에 대해서도 파라미터로(다시말해 참조로) 다 넘기기면, 콜 스택에 불필요하게 상태값을 저장하지 않는다. 백트랙할 필요가 없다는 것은 결과값을 바로 스택에 받고 리턴받고할 수 있다는 점이다.

- Because there is a fundamental difference between head recursion and tail recursion.
  - tail recursion related function calls (and the stack frames) do not depend on each other - there is no so-called "downward dependence" in the stack memory regarding the stack frames
  - head recursion related function calls DO depend on each other - they use values returned from other function calls
- This is exactly why we can optimise tail recursion because the function calls and stack frames are totally independent of each other.
