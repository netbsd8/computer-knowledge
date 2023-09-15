from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ""
        for s in strs:
            cur = str(len(s)) + '||' + s
            ret = ret + cur
        return ret

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i, j = 0, 0
        ret = []

        while True:
            pos = s.find('||')
            if pos == -1:
                break
            count = int(s[0:pos])
            next_pos = pos + 2 + count
            ret.append(s[pos+2: next_pos])
            s = s[next_pos:]

        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))