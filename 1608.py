class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)  # Total numbers in the list

        # Try each number from 0 to n
        for x in range(n + 1):
            count = 0  # Count how many numbers >= x

            # Count numbers greater than or equal to x
            for num in nums:
                if num >= x:
                    count += 1

            # If exactly x numbers are >= x, return x
            if count == x:
                return x

        # If no x satisfies the condition, return -1
        return -1