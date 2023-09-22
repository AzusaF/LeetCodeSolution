class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rc = [''] * n
        for i in range(1,n+1,1):
            if i % 15 == 0:
                rc[i-1] = "FizzBuzz"
            elif i % 5 == 0:
                rc[i-1] = "Buzz"
            elif i % 3 == 0:
                rc[i-1] = "Fizz"
            else:
                rc[i-1] = str(i)
        return rc