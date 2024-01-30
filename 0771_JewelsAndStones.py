'''
Runtime
14
ms
Beats
67.95%
of users with Python
---
Memory
11.77
MB
Beats
89.13%
of users with Python
'''
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        numOfJewels = 0
        originalStones = stones
        for jewel in jewels:
            # print(jewel)
            idx = 0
            stones = originalStones
            while idx != -1:
                # print(stones)
                # print(jewel)
                # print(idx)
                idx = stones.find(jewel)
                if idx != -1:
                    stones = stones[(idx+1):]
                    numOfJewels += 1
        return numOfJewels
