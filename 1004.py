class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,zero,length,maxlength=0,0,0,0
        size=len(nums)
        for right in range(size):
            if nums[right]==0:
                zero+=1
            if zero>k:
                while nums[left]!=0:
                    left+=1
                left+=1
                zero-=1
            length=right-left+1
            maxlength=max(maxlength,length)
        return maxlength