import random


class RandomizedSet:

    def __init__(self):
        self._m = {}
        self._data = []
        

    def insert(self, val: int) -> bool:
        if val not in self._m:
            self._data.append(val)
            self._m[val] = len(self._data) - 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val not in self._m:
            return False

        o_index = self._m[val]
        # order is important, for instance: single item
        self._data[o_index] = self._data[-1]
        self._m[self._data[-1]] = o_index
        del self._m[val]
        self._data.pop(-1)
        return True
        

    def getRandom(self) -> int:
        r_index = random.randint(0, len(self._data)-1)
        return self._data[r_index] 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()