class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        temp = [0]*len(arr)
        j = 0
        for i in range (0, len(arr), 1):
            if j >= len(arr):
                break
            if arr[i] == 0:
                temp[j] = 0
                if j + 1 >= len(arr):
                    break
                temp[j + 1] = 0
                j +=2
            else:
                temp[j] = arr[i]
                j +=1
        for i in range (0, len(arr), 1):
            arr[i] = temp[i]