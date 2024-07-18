class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        length = len(s)
        i = 0
        while i < length:
            num = dict[s[i]]
            if i+1 < length:
                num2 = dict[s[i+1]]
                if (num == 1 and (num2 == 5 or num2 == 10)) or (num == 10 and (num2 == 50 or num2 == 100)) or (num == 100 and (num2 == 500 or num2 == 1000)):
                    result -= num
                else:
                    result += num
            else:
                result += num
            i += 1
        return result
