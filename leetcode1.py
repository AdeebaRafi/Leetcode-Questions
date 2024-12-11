class Solution:
    def twoSum(self, nums, target):  # Change method name to twoSum
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Test the function
sol = Solution()
nums = [1, 7, 11, 6]
target = 13
result = sol.twoSum(nums, target)  # Call twoSum, not two_sum
print(result)
