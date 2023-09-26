class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        nums[0] = nums[0]
        for i in range(1,len(nums),1):
            # print(nums[i])
            if nums[i] != nums[i-1]:
                k += 1
                # print("unique")
                # print("nums[k]:", nums[k])
                # print("nums[i]:", nums[i])
                # print("k:", k)
                # print("i:", i)
                nums[k-1] = nums[i]
        return k