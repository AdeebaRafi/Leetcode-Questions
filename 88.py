class Solution:
    def merge(self, nums1, m, nums2, n):
        # Start filling from the end
        i = m - 1  # last element of nums1's actual data
        j = n - 1  # last element of nums2
        k = m + n - 1  # last index of nums1 total space

        # Compare from the end and fill backwards
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
