import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = s.lower().strip()
        str = re.sub(r'[^a-z0-9]', '', str)
        front = 0
        back = len(str)-1
        if back == 0:
            return True
        # print(str)
        while front < back:
            # print(front)
            # print(back)
            # print(str[front])
            # print(str[back])
            if (back - front) == 1 and str[front] != str[back]:
                return False
            elif str[front] != str[back]:
                return False
            else:
                front +=1
                back -= 1
        return True