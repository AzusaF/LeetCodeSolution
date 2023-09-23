class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for i in range(0,len(accounts),1):
            sum = 0
            for j in range(0,len(accounts[i]),1):
                sum += accounts[i][j]
            if sum > richest:
                richest = sum
        return richest