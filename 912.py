class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: If the array has 0 or 1 element, it's already sorted
        if len(nums) <= 1:
            return nums

        # Step 1: Divide the array into two halves
        mid = len(nums) // 2
        left = nums[:mid]     # Left half
        right = nums[mid:]    # Right half

        # Step 2: Recursively sort both halves
        self.sortArray(left)
        self.sortArray(right)

        # Step 3: Merge the two sorted halves
        i = j = k = 0  # i for left, j for right, k for nums

        # Merge elements from left and right in sorted order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements from left (if any)
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements from right (if any)
        while j < len(right):  # Corrected: changed 'left' to 'right'
            nums[k] = right[j]
            j += 1
            k += 1

        # Return the sorted array
        return nums