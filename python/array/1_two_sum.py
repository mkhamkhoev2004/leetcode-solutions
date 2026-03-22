# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in m:
                return [m[complement], i]
            m[num] = i
        return None