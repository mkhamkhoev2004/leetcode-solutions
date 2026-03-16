// Time Complexity: O(n)
// Space Complexity: O(n)
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	return numsToBST(nums, 0, len(nums)-1)
}

func numsToBST(nums []int, left, right int) *TreeNode {
	if left > right {
		return nil
	}

	mid := left + (right-left)/2

	node := &TreeNode{}

	node.Val = nums[mid]
	node.Left = numsToBST(nums, left, mid-1)
	node.Right = numsToBST(nums, mid+1, right)

	return node
}
