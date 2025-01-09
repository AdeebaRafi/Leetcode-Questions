class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for i in words: #O(n)
            if pref== i[0:len(pref)]:# slicing has complexity of O(n) but n is already assigned so we consider O(m) where m is length of pref
                ans+=1
        return ans