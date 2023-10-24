# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        mid = 0
        right = n
        result = 0
        while left <= n:
            mid = left + (right - left)/2
            result = guess(mid)
            if result is -1:
                right = mid - 1
            elif result is 1:
                left = mid + 1
            else:
                return mid