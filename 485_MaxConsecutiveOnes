class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        max = 0
        for i in range(0, len(nums), 1):
            if nums[i] == 0:
                j = 0
            else:
                j += 1
                if j > max:
                    max = j
        return max