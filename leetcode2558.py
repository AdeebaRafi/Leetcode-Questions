import heapq
import math


def remainingGifts(gifts, k):
    # Create a max-heap by pushing negative values
    max_heap = [-gift for gift in gifts]
    heapq.heapify(max_heap)

    # Perform k operations
    for _ in range(k):
        # Pop the largest pile (convert back to positive)
        largest = -heapq.heappop(max_heap)
        # Calculate the floor of its square root
        leftover = math.floor(math.sqrt(largest))
        # Push the leftover back into the heap as negative
        heapq.heappush(max_heap, -leftover)

    # Calculate the total remaining gifts
    return sum(-gift for gift in max_heap)


# Example 1
gifts = [25, 64, 9, 4, 100]
k = 4
print(remainingGifts(gifts, k))  # Output: 29

# Example 2
gifts = [1, 1, 1, 1]
k = 4
print(remainingGifts(gifts, k))  # Output: 4

#leetcode
# import heapq
# # heap
# class Solution(object):
#     def pickGifts(self, gifts, k):
#         """
#         :type gifts: List[int]
#         :type k: int
#         :rtype: int
#         """
#         for i, x in enumerate(gifts):
#             gifts[i] = -x
#         heapq.heapify(gifts)
#         for _ in xrange(k):
#             x = heapq.heappop(gifts)
#             heapq.heappush(gifts, -int((-x)**0.5))
#         return -sum(gifts)