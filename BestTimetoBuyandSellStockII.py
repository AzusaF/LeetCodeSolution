class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        for i in range(0, len(prices), 1):
            for j in range(0, len(prices), 1):
                print("prices[i]: ", prices[i])
                print("prices[j]: ", prices[j])
                if max < prices[j] - prices[i]:
                    print('max updated to ', prices[j] - prices[i])
                    max = prices[j] - prices[i]
        return max