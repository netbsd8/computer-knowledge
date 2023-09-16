class Solution:
    # no convert to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        orig = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10

        return rev == orig
        
    # convert to string
    def isPalindrome_2(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)
        l, r = 0, len(x_str)-1
        while l < r:
            if x_str[l] != x_str[r]:
                return False
            l += 1
            r -= 1
        return True