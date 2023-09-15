import collections
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)

        for path in paths:
            p = path.split()
            dir, rest = p[0], p[1:]
            for f in rest:
                file_name, file_content = f.split('(')[0], f.split('(')[1][:-1]
                m[file_content].append(f"{dir}/{file_name}")

        return [m[k] for k in m.keys() if len(m[k]) > 1]
