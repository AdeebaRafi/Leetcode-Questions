class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            # Convert number n to the string representation in the given base
            rep = ""
            num = n
            while num:
                rep += str(num % base)
                num //= base

            # Check if the base representation is not palindromic
            if not self.isPalindrome(rep):
                return False

        return True