class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count_array = [0] * 101
        for num in nums:
            count_array[num] += 1
        for count in count_array:
            res += (count * (count - 1)) // 2
        return res