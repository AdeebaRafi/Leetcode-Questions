from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                # Swap and invert elements at left and right
                # When left == right, handle middle element in odd length row
                if left == right:
                    row[left] ^= 1  # Just invert
                else:
                    # Swap and invert both ends
                    row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left += 1
                right -= 1
        return image
