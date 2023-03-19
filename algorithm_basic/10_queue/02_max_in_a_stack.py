# 스택의 최고값을 가지고있는 스택을 만드시오
# O(n) 만큼의 공간을 하나 더 갖고,
# 데이터가 들어있는 값의 스택을 넣을 때 같이 관리하면 O(1)만에 해결


class MaxStack:
    def __init__(self) -> None:
        self.stack = []
        self.max_val = []

    def push(self, value):
        if 0 == len(self.stack):
            self.stack.append(value)
            self.max_val.append(value)

        else:
            if self.stack[-1] > value:
                self.stack.append(value)
                self.max_val.append(self.max_val[-1])
            else:
                self.stack.append(value)
                self.max_val.append(value)

    def pop(self):
        self.stack.pop()
        return self.max_val.pop()

    def peek(self):
        return self.max_val[-1]


m = MaxStack()
m.push(3)
print(m.peek())
m.push(7)
print(m.peek())
m.push(4)
print(m.peek())
m.push(10)
print(m.peek())
m.push(11)
print(m.peek())
m.push(-1)
print(m.peek())
