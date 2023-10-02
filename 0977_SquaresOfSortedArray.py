#Merge Sort
def mergeSort(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)
       i=0
       j=0
       k=0
       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1
       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1
       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums), 1):
            nums[i] = nums[i]*nums[i]
            
        mergeSort(nums)
        return nums
        