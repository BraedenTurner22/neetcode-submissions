class MinStack:

    def __init__(self):
        self.stack = []
        self.minAtIndex = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minAtIndex:
            if self.minAtIndex[-1] <= val:
                self.minAtIndex.append(self.minAtIndex[-1])
            else:
                self.minAtIndex.append(val)
        else:
            self.minAtIndex.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minAtIndex.pop() 

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minAtIndex[-1]
