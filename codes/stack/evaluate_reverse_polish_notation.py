from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ret = 0
        st = []
        i = 0

        for i in range(len(tokens)):
            if tokens[i] in ['*', '/', '+', '-']:  # "-11".isdigit() return False
                val1 = st.pop()
                val2 = st.pop()

                if tokens[i] == '+':
                    ret = val1 + val2
                elif tokens[i] == '-':
                    ret = val2 - val1
                elif tokens[i] == '*':
                    ret = val2 * val1
                elif tokens[i] == '/':
                    ret = int(float(val2)/val1)
                st.append(ret)
                continue

            val = int(tokens[i])
            st.append(val)

        return st[0]