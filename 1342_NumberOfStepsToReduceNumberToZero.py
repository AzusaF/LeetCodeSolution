class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        rc = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num -1
            rc += 1
        return rc