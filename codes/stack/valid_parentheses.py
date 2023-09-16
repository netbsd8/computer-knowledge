class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                if c == ')' and st[-1] != '(':
                    return False
                elif c == ']' and st[-1] != '[':
                    return False
                elif c == '}' and st[-1] != '{':
                    return False
                else:
                    st.pop()

        return len(st) == 0
        