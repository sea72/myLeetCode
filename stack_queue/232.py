class MyQueue:

    def __init__(self):
        self.que = []
        self.size = 0


    def push(self, x: int) -> None:
        self.que.append(x)
        self.size += 1


    def pop(self) -> int:
        temp = self.que[0]
        self.que = self.que[1:]
        self.size -= 1
        return temp

    def peek(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return self.size > 0




obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print('h')