def solution(
    disk,
    source,
    middle,
    destination
):
    """ 하노이의 탑 구현

    큰 문제를 작은 문제로 나누어 연산하게 한다
    """
    if disk == 0:
        print(f"move disk {disk} from {source} to {destination}")
        return

    # 중간 갔다가 
    solution(disk - 1, source, destination, middle)
    print(f"move disk {disk} from {source} to {destination}")
    solution(disk - 1, middle, source, destination)



solution(64, 'A', 'B', 'C')
