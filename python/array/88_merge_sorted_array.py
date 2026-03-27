# Time Complexity: O(n + m)
# Space Complexity: O(1)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        i = len(nums1) - 1

        while n >= 0:
            if m > 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
        i -= 1