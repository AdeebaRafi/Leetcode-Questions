class Solution:
    def longestCommonSubsequence(self,text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(i,j):
            # Base Case: reached the end of either string
            if i == len(text1) or j == len(text2):
                return 0
            # Characters match
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            # Try skipping either character
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)