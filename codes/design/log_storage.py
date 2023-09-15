from typing import List


class LogSystem:

    def __init__(self):
        self.logs = []
        

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        index = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}[granularity]
        s = start[:index]
        e = end[:index]
        
        return sorted(tid for tid, timestamp in self.logs
                      if s <= timestamp[:index] <= e)  



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)