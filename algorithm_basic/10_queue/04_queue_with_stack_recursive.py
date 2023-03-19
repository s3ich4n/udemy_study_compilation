#
# enqueue() 호출시
#   1. enqueue stack에 스택처럼 쌓기
# dequeue() 호출시
#   1. enqueue stack의 맨위를 계속 pop 하기
#      dequeue stack에 뒤집어서 넣기
#      그래야 stack처럼 쓰는거고, 논리적으로 말이맞음
#   2. dequeue stack이 비면, 1을 또 해서 dequeue stack을 채우기
#
#


class QueueWithStack:
    def __init__(self) -> None:
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if not len(self.enqueue_stack) and not len(self.dequeue_stack):
            raise Exception("stack is empty")

        if 0 == len(self.dequeue_stack):
            while 0 != len(self.enqueue_stack):
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()


q = QueueWithStack()
q.enqueue(10)
q.enqueue(5)
q.enqueue(20)
print(f"dequeue: {q.dequeue()}")

q.enqueue(100)
print(f"dequeue: {q.dequeue()}")
print(f"dequeue: {q.dequeue()}")
print(f"dequeue: {q.dequeue()}")
print(f"dequeue: {q.dequeue()}")
