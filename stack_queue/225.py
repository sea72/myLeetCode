from collections import deque
class MyStack1:

    def __init__(self):
        self.stackLhs = deque()
        self.stackRhs = deque()

    def push(self, x: int) -> None:
        self.stackRhs.append(x)

    def pop(self) -> int:
        if self.stackRhs:
            while True:
                temp = self.stackRhs.popleft()
                if self.stackRhs:
                    self.stackLhs.append(temp)
                else:
                    return temp
        else:
            while True:
                temp = self.stackLhs.popleft()
                if self.stackLhs:
                    self.stackRhs.append(temp)
                else:
                    return temp        

    def top(self) -> int:
        temp = self.pop()
        self.push(temp)
        return temp


    def empty(self) -> bool:
        return len(self.stackLhs) == 0 and len(self.stackRhs) == 0

class MyStack:

    def __init__(self):
        self.deque1 = deque()
        self.deque2 = deque()

    def push(self, x: int) -> None:
        self.deque2.append(x)
        while self.deque1:
            self.deque2.append(self.deque1.popleft())
        self.deque1, self.deque2 = self.deque2, self.deque1
    
    def pop(self) -> int:
        return self.deque1.popleft()

    def top(self) -> int:
        return self.deque1[0]

    def empty(self) -> bool:
        return not self.deque1

myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()
myStack.pop()
print(myStack.empty())

