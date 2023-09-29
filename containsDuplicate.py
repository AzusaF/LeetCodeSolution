class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = [None]*len(nums)
        unique[0] = nums[0]
        k = 1
        print(len(nums))
        print(len(unique))
        for i in range(1,len(nums),1):
            for j in range(0, k, 1):
                if nums[i] == unique[j]:
                    return True
            unique[k] = nums[i]
            k += 1
            # if k > len(nums):
            #     return False
            # print(k)
        return False