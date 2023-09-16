class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carrier = 0
        ret = ""
        len_a = len(a)
        len_b = len(b)
        count = 0
        new_a = a[::-1]
        new_b = b[::-1]
        for i in range(min(len_a, len_b)):
            c1 = int(new_a[i])
            c2 = int(new_b[i])
            ret = str((c1+c2+carrier)%2) + ret
            carrier = (c1+c2+carrier) // 2
            count += 1
        print(ret)

        if count < len_a:
            for i in range(count, len_a):
                c1 = int(new_a[i])
                ret = str((c1+carrier)%2) + ret
                carrier = (c1+carrier) // 2
        if count < len_b:
            for i in range(count, len_b):
                c2 = int(new_b[i])
                ret = str((c2+carrier)%2) + ret
                carrier = (c2+carrier) // 2

        if carrier:
            ret = '1' + ret

        return ret