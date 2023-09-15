class Logger:

    def __init__(self):
        self.m = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.m:
            self.m[message] = timestamp
            return True

        if self.m[message] + 10 <= timestamp:
            self.m[message] = timestamp
            return True

        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)