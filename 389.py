class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total = 0
        for ch in t:
            total += ord(ch)
        for ch in s:
            total -= ord(ch)
        return chr(total)
