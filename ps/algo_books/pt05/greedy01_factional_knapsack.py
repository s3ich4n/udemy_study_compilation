def fractional_knapsack(capacity: int, cargo):
    cap: int = capacity
    pack = []

    # 단가 계산 역순정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    total_value: float = 0
    for p in pack:
        # 그냥 자기 값 대로 넣음
        if cap - p[2] >= 0:
            cap -= p[2]
            total_value += p[1]
        # 쪼개서 넣음
        else:
            fraction = cap / p[2]
            total_value += p[1] * fraction
            break

    return total_value


print(fractional_knapsack(12, [(4,12), (2,1), (10,4), (1,1), (2,2)]))
