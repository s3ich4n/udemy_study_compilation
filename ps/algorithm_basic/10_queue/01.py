import collections


class Queue:
    def __init__(self) -> None:
        self.queue = collections.deque()

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return 0 == len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(f"size: {len(queue)}")
print(f"dequeue: {queue.dequeue()}")
print(f"size: {len(queue)}")
print(f"peek: {queue.peek()}")
print(f"size: {len(queue)}")
