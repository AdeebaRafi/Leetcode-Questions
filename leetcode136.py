class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        newset=set(nums)
        print(newset)
        print(type(newset))
        for i in newset:
            if nums.count(i) == 1:
                return i