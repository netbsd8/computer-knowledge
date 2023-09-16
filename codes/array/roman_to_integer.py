class Solution:
    # Solution 2 -- substraction
    def romanToInt_2(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

        i = 0
        val = 0
        while i < len(s):
            if i+1 < len(s) and m[s[i]] < m[s[i+1]]:
                val += m[s[i+1]] - m[s[i]]
                i += 2
            else:
                val += m[s[i]]
                i += 1

        return val

    # Solution 1 -- all addition
    def romanToInt_1(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
            }

        i = 0
        val = 0
        while i < len(s):
            if i <= len(s) - 2 and s[i:i+2] in m: 
                val += m[s[i:i+2]]
                i += 2
            else:
                val += m[s[i]]
                i += 1

        return val