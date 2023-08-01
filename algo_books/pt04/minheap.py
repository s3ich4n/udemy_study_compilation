class BinaryHeap:
    def __init__(self) -> None:
        self.items = [None]     # 0번 값은 비워둠

    def __len__(self) -> int:
        return len(self.items) - 1

    def _percolate_up(self):
        """
        힙에 요소를 삽입(up-heap)한다.
        
        1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입한다
            (배열일 때는 가장 마지막에 삽입)
        2. 부모 값과 비교하여 값이 더 작은 경우 위치를 변경한다
        3. 계속해서 부모값과 비교하여 위치를 변경한다
            (가장 작은값이면 루트까지 올라감)
        """
        length = len(self)

        parent = length // 2

        while parent > 0:
            if self.items[parent] > self.items[length]:
                self.items[parent], self.items[length] = self.items[length], self.items[parent]

            length = length // 2
            parent = length // 2
        
    def _percolate_down(self, i):
        """

        min heap에서 요소를 제거한다.

        1. 루트값을 별도로 분리한다
        2. 새 루트값을 현재 최소힙의 가장 작은 변수로 지정한다
        3. 최소힙의 트리 끝까지 내려가면서 부모-자식간 높낮이를 맞춘다
            1. 높낮이를 맞추면 스왑하여 처리하고
            2. 다시 재귀하여 자식 노드를 쫓아간다

        """
        left = 2 * i
        right = (2 * i) + 1
        smallest = i

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        
        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self._percolate_down(smallest)

    def push(self, element):
        self.items.append(element)
        self._percolate_up()

    def pop(self) -> int:
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted


b = BinaryHeap()
b.push(10)
b.push(6)
b.push(4)
b.push(2)
b.push(5)
b.push(3)
b.pop()
print(len(b))
