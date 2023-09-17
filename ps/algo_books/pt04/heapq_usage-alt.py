#
# source:
#   https://realpython.com/python-heapq-module/#example-finding-paths
#
#   .은 빈공간이고, x는 장애물이다.


import heapq

map = """\
...X.
.XXX.
.XXX.
.....
"""

#
# 1. 후보군에서 후보값을 꺼내고
# 2. '확실한' 최단거리에 값이 있는지 비교. 없으면 아래 과정대로, 있으면 스킵
# 3. 현재 후보에서 가장 짧은 값을 찾음
# 4. 후보군의 최단거리에 대해, '잠정적인' 값보다 짧으면
#    현재 '잠정적인' 값을 방금 발견한 최단거리로 바꾼다
#


def parse_map(map):
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination


def is_valid(lines, position):
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    # y값이 먼저 커지고(inner for loop), x값은 나중에 커진다(outer for loop).
    # 즉, get_neighbors에서 계산하는 식으로 좌표값 내 값을 비교하려면, 이렇게 비교한다.
    if lines[y][x] == "X":
        return False
    return True


def get_neighbors(lines, current):
    """
    8 방으로 다니면서 갈 수 있는 길인지 찾는다.
    -1, 0, 1 이런식으로 dx 및 dy를 -1, 0, 1 좌표로 처리하고
    is_valid로 유효한 좌표값인지 알아본 후 position을 yield한다
    """
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 and dy == 0) or (abs(dx) + abs(dy) == 2):
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position


def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):  # 왔던길 혹은 더 긴 후보길은 쫓아갈 필요가 없다
            continue
        yield position, path


def find_path(map):
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}                        # 잠정적 경로 저장소
    candidates = [(0, origin)]                      # 후보군에 대해 minheap으로 처리하기 위해
    certain = set()                                 # 유일하고 확정된 값이어야하니까

    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain    # 확실한 값을 뺀 "진행가능한" 이웃값
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))

    if destination in tentative:
        return tentative[destination] + [destination]

    else:
        raise ValueError("no path")


def show_path(path, map):
    print("길찾기 시작")
    print(map)

    print("\n ---- \n길 찾음! 아래의 루트:")

    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + "@" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"


path = find_path(map)
print(show_path(path, map))
