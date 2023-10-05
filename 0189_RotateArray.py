class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length= len(nums)
        temp = [0]*length
        print(length)
        for i in range (0,length,1):
            if k > i:
                # print("k>i")  
                # print("length-1-k+i:", length-k+i)
                temp[i] = nums[length-k+i]
            else:
                temp[i] = nums[i-k]
        # print(temp)
        # print(nums)
        nums = temp
        print(nums)