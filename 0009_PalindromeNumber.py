class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = ''
        string = str(x) 
        j = len(string) - 1
        for i in range(0, len(string)/2):
            if (len(string)-1) == len(string)/2:
                if string[0] != string[1]:
                    return False
                else:
                    return True
            if string[i] != string[j]:
                return False
            j-=1
        return True