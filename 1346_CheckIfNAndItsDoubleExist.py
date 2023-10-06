class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        rc = False
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if i != j and 0 <= i and j < len(arr) and arr[i] == 2 * arr[j]:
                    rc = True
        return rc