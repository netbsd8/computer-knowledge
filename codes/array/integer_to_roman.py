class Solution:
    # using internal property
    def intToRoman(self, num: int) -> str:
        m = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ret = ""
        for v, r in zip(values, romans):
            while num >= v:
                ret += r
                num -= v
        # while num > 0:
        #     for v, r in zip(values, romans):
        #         while num >= v:
        #             ret += r
        #             num -= v


        return ret


    ## the following shows how hard to cover all the use cases
    # def intToRoman(self, num: int) -> str:
    #     ret = ""
    #     ones = num % 10
    #     tens = (num - ones) % 100
    #     hundreds = (num - ones - tens) % 1000
    #     thousands = (num - oness - tens - hundreds) % 10000

    #     num_str = str(num)

    #     for i in range(len(num_str)):
    #         cur = ""
    #         if int(num_str(i)) == 4:
    #         ret += cur

    #     d = 1000
    #     while num > 0:
    #         cur = num // d
    #         num = num % d
    #         d = d / 10
        
    #     return ret