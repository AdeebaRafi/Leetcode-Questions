class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will hold all the subsets

        subset = []  # Temporary list to store the current subset

        def dfs(i):
            # Base case: if we've considered all elements
            if i == len(nums):
                res.append(subset.copy())  # Add a copy of the current subset to the result
                return

            # -------- Decision to INCLUDE nums[i] in the subset --------
            subset.append(nums[i])      # Include nums[i]
            dfs(i + 1)                  # Move to the next element

            # -------- Decision to EXCLUDE nums[i] from the subset --------
            subset.pop()               # Backtrack: remove the last added element
            dfs(i + 1)                 # Move to the next element

        dfs(0)  # Start the recursion from index 0
        return res  # Return all the generated subsets