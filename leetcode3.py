class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize variables
        char_set = set()
        start = 0
        max_length = 0

        # Use the end pointer to iterate through the string
        for end in range(len(s)):
            # If a duplicate character is found, shrink the window
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1

            # Add the current character to the set
            char_set.add(s[end])
            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)

        return max_length

# Example usage
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
