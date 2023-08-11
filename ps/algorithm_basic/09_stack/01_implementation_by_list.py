class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if 0 == len(self.stack):
            return

        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push('1st')
stack.push('2nd')
stack.push('3rd')
stack.push('4th')

print(f"size: {len(stack)}")
print(f"popped: {stack.pop()}")
print(f"size: {len(stack)}")
print(f"peeked: {stack.peek()}")
print(f"size: {len(stack)}")
print(f"popped: {stack.pop()}")
print(f"size: {len(stack)}")
