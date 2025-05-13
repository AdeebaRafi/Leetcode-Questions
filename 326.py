class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3  # Integer division

        return n == 1