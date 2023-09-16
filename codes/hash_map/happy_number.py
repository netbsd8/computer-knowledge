class Solution:
    # Python method
    def isHappy(self, n: int) -> bool:
        m = set()

        while n != 1:
            if n in m:
                return False
            m.add(n)

            n = sum([int(i)**2 for i in str(n)])

        return True

    # general method
    def isHappy_2(self, n: int) -> bool:
        m = set()
        val = n

        while val not in m:
            m.add(val)
            summ = 0
            
            while val > 0:
                summ = summ + (val%10)**2
                val //= 10

            if summ == 1:
                return True

            val = summ

        return False
        