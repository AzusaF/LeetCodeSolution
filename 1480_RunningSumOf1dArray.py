class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rc = [0] * len(nums)
        rc[0] = nums[0]
        i = 1
        for i in range(1,len(nums),1):
            rc[i] = rc[i-1] + nums[i]
        return rc