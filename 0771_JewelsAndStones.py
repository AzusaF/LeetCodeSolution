'''
Runtime
11
ms
Beats
85.04%
of users with Python
---
Memory
11.59
MB
Beats
98.53%
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
        for jewel in jewels:
            numOfJewels += stones.count(jewel)
        return numOfJewels
