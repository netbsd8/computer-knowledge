class Solution:
    def calculate(self, s: str) -> int:
        st = []
        s = s.strip()
        for idx, c in enumerate(s):
            if c == ')':
                summ = self.getSum(st)
                if st and st[-1] == '(':
                    st.pop() # pop '('
                for cc in list(str(summ)):
                    st.append(cc)
            else:
                if c == ' ':
                    continue
                st.append(c)


        # in case no '()' in the expression
        summ = self.getSum(st)
        for cc in list(str(summ)):
            st.append(cc)

        ret = "".join(st)
        return int(ret)

    def getSum(self, st):
        summ = 0
        while st:
            if st[-1] == '(':
                break
            val = 0
            i = 0
            while st and st[-1].isdigit():
                val += int(st[-1]) * (10 ** i)
                i += 1
                st.pop()
            while st and st[-1] in ['-', '+']:
                if st[-1] == '-':
                    val = -1 * val;
                st.pop() # pop '+' or '-'
            summ += val

        return summ