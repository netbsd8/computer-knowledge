class MinStack:

    def __init__(self):
        self.st = []
        self.mt = []
        
    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.mt or val < self.mt[-1]:
            self.mt.append(val)
        else:
            self.mt.append(self.mt[-1])
        
    def pop(self) -> None:
        val = self.st[-1]
        self.st.pop()
        self.mt.pop()
        

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mt[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()