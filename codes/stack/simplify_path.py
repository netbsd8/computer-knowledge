class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []

        i = 0
        while i < len(path):
            if path[i] == '/':
                i += 1
                continue

            # count = 0
            # while i < len(path) and path[i] == '.':
            #     count += 1
            #     i += 1
            # if count == 1:
            #     continue
            # elif count == 2:
            #     if st:
            #         st.pop()
            # elif count > 2:
            #     word = '.' * count
            #     st.append(word)

            word = ""
            while i < len(path) and path[i] != '/':
                word += path[i]
                i += 1
            if word == '.':
                continue
            elif word == '..':
                if st:
                    st.pop()
            elif len(word) > 0:
                st.append(word)

        ret = "/"
        if not st:
            return ret
        return ret + '/'.join(st) 