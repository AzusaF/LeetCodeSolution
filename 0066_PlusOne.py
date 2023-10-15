class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        digits[idx] = digits[idx] + 1
        while digits[idx] == 10 and idx >= 0:
            digits[idx] = 0
            if idx == 0:
                digits.insert(0,1)
            else:
                digits[idx-1] = digits[idx-1] + 1
            idx -= 1
        return digits