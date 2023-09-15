import collections
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)

        for string in strings:
            cur_pattern = self.getPattern(string)
            # print(f"{string}, {cur_pattern}")
            m[cur_pattern].append(string)

        return list(m.values())

    def getPattern(self, cur):
        pattern = ""
        
        c = cur[0]
        for v in cur[1:]:
            pattern += str((ord(v) - ord(c))%26) # handle 'az' --> 'ba'
            pattern += '+' # handle 'abc' --> 'al' all have 11
            c = v

        return pattern

    # def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # ret = []
        # m = collections.defaultdict(list)

        # for string in strings:
        #     l = len(string)
        #     m[l].append(string)

        # for k, v in m.items():
        #     # if len(v) == 1:
        #     #     ret.append(v[0])
        #     #     continue
        #     s = set(v) # <-- not good for same item
        #     while True:
        #         if len(s) == 0:
        #             break

        #         cur = list(s)[0]
        #         pattern = self.getPattern(cur)
        #         ans = [cur]
        #         s.discard(cur)

        #         s_list = list(s)
        #         for string in s_list:
        #             cur_pattern = self.getPattern(string)
        #             if cur_pattern == pattern:
        #                 ans.append(string)
        #                 s.discard(string)

        #         ret.append(ans)
        # return ret



            # s = set(v)
            # while s:
            #     cur = list(s)[0]
            #     q = deque()
            #     q.append(cur)
            #     ans = []
            #     while q:
            #         t = q.popleft()
            #         ans.append(t)
            #         s.discard(t)

            #         left = ""
            #         right = ""
            #         for c in t:
            #             if c == 'a':
            #                 left += 'z'
            #             else:
            #                 left += chr(ord(c)-1)
            #             if c == 'z':
            #                 right += 'a'
            #             else:
            #                 right += chr(ord(c)+1)

            #         if left in s:
            #             q.append(left)
            #         if right in s:
            #             q.append(right)
                
        #         ret.append(ans)

        # return ret