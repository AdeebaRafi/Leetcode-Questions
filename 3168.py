class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        max_count = 0
        for i in range(len(s)):
            if s[i] == "E":
                count += 1
                max_count = max(max_count, count)

            if s[i] == "L":
                count -= 1
        return max_count

# Time Complexity: O(n)
# Space Complexity: O(1)