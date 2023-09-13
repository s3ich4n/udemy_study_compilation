def zero_one_knapsack(capacity: int, cargo):
    pack = []

    # 타뷸레이션을 위한 테이블을 미리 만들기
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            # 아무것도 가방에 안 넣으면 0이니까 이를 채워넣는다.
            if i == 0 or c == 0:
                pack[i].append(0)
            
            # 가방에서 꺼낸 값이
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i-1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])

    # 최적의 이익은 기존 정보(된다고 판단한 값)에서 계속 더해왔던 값임
    return pack[-1][-1]


print(zero_one_knapsack(15, [(4,12), (2,1), (10,4), (1,1), (2,2)]))
