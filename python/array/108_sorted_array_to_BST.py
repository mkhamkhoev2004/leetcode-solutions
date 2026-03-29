# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def numsToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            
            node = TreeNode(nums[mid])
            node.left = numsToBST(left, mid - 1)
            node.right = numsToBST(mid + 1, right)
            
            return node
        
        return numsToBST(0, len(nums) - 1)