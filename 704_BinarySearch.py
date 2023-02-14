class Solution(object):
    def search(self, nums, target):
        low_index = 0
        high_index = len(nums)-1
        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2
            if target == nums[mid_index]:
                return mid_index
            if target > nums[mid_index]:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1
        return -1