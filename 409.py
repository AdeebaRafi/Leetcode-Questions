from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False

        for cnt in counts.values():
            if cnt % 2 == 0:
                length += cnt
            else:
                length += cnt - 1  # use the even part
                has_odd = True

        if has_odd:
            length += 1  # put one odd-count letter in the center

        return length
