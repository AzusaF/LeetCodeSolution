class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rc = [0]*2
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    rc[0] = i
                    rc[1] = j 
                    return rc