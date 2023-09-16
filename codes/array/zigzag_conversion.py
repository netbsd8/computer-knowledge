class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = ["" for _ in range(numRows)]
        i = 0
        while i < len(s):
            j = 0
            while j < numRows:
                ret[j] += s[i]
                j += 1
                i += 1
                if i == len(s):
                    return "".join(ret)
            # print(ret)
            # Note: roll back 2 steps
            j -= 2
            while j > 0:
                ret[j] += s[i]
                j -= 1
                i += 1
                if i == len(s):
                    return "".join(ret)
            # print(ret)

        return "".join(ret)