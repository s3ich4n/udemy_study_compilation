def permutation(n, r, memo):
    if r == 0:
        return 1
    if n < r:
        return 0
    if (n, r) in memo:
        return memo[(n, r)]
    
    # 계산하지 않은 경우, 재귀적으로 계산
    result = n * permutation(n - 1, r - 1, memo) + permutation(n - 1, r, memo)
    
    memo[(n, r)] = result  # 결과를 메모이제이션
    return result


def main():
    n = 6  # 예: 6개의 항목 중
    r = 2  # 2개의 항목을 선택하는 순열 계산
    
    memo = {}  # 메모이제이션 테이블
    
    result = permutation(n, r, memo)
    
    print(f"P({n}, {r}) = {result}")


if __name__ == "__main__":
    main()
