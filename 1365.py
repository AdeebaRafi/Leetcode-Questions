from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # ====================== Approach no. 1 ==================
        d = Counter(nums)

        result = []

        for i in nums:
            count = 0
            for j in d.keys():
                if j < i:
                    count += d[j]
            result.append(count)
        return result