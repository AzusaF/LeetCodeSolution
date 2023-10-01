class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numOfDigits = 1
        even = 0
        for i in range(0, len(nums), 1):
            while nums[i]/10 > 0:
                print(nums[i])
                nums[i] = nums[i]/10
                numOfDigits += 1
            if numOfDigits != 0 and numOfDigits%2 == 0:
                even += 1
            numOfDigits = 1
        return even