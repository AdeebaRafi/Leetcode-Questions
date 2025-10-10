class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        j = 0  # pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move in s if characters match
            j += 1  # always move in t

        return i == len(s)