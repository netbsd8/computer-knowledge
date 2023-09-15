class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = 0
        self.length = len(compressedString)
        self.cur = None
        self.cnt = 0
        self.data = compressedString
        

    def next(self) -> str:
        if self.cnt != 0:
            self.cnt -= 1
            return self.cur

        if self.idx == self.length:
            return " "

        self.cur = self.data[self.idx]
        self.idx += 1

        pos = self.idx
        while pos < self.length and self.data[pos].isdigit():
            pos += 1

        self.cnt = int(self.data[self.idx:pos]) - 1
        self.idx = pos
        return self.cur
            
        

    def hasNext(self) -> bool:
        if self.cnt == 0 and self.idx == self.length:
            return False
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()