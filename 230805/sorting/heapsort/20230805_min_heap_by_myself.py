import cProfile
import timeit
import heapq
# import sys

from typing import List, Optional

from utils import make_array


class UserHeap:
    capacity: int
    power: int
    heap: List[Optional[Optional[int]]]

    def __init__(self):
        self.heap = [None]
        self.capacity = 1
        self.power = 2 ** 0

    def __len__(self):
        return len(self.heap) - 1

    def heappush(self, val: int):
        self.heap.append(val)
        heap_size = len(self)
        parent = heap_size // 2

        while parent > 0:
            if self.heap[parent] > self.heap[heap_size]:
                self.heap[parent], self.heap[heap_size] \
                    = self.heap[heap_size], self.heap[parent]

            heap_size = heap_size // 2
            parent = heap_size // 2

        self.capacity += 1

    def heappop(self) -> int:
        result = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.capacity -= 1

        i = 1

        while True:
            left = (2 * i)
            right = (2 * i) + 1
            smallest = i

            if left <= len(self) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right <= len(self) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                i *= 2

            else:
                break

        return result


# 1 부터 시작하는 배열
heap = UserHeap()

# a = make_array(1_000_000, 1_000_000_000)
a = make_array(9, 100)
# a = [52, 49, 5, 3, 11, 26, 77, 48, 6]


def do_the_heap_sort():
    for x in a:
        heap.heappush(x)


do_the_heap_sort()
print(f"origin array: {a}")
heapq.heapify(a)


for _ in range(0, 9):
    print(f"heapq.heappop(): {heapq.heappop(a):5} \t"
          f"| UserHeap.heappop(): {heap.heappop():5}")


# 1. timeit으로 수행시간 테스트. 아래와 같이 실행함:
# execution_time = timeit.timeit(
#     "do_the_heap_sort()",
#     globals=globals(),
#     number=1,
# )
# print(f"quicksort() execution time: {execution_time}")

# 2. cProfile로 어떤 구문이 얼마만큼 실행되었는지 프로파일링
#    stdout으로 실행내용이 나옴. 아래와 같이 실행함:
# cProfile.run("do_the_heap_sort()")
