class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [0] * 26  # Array of size 26 to mark seen letters

        for char in sentence:
            idx = ord(char) - ord('a')  # Map 'a' → 0, ..., 'z' → 25
            seen[idx] = 1  # Mark this letter as seen

        return sum(seen) == 26  # If all 26 letters seen