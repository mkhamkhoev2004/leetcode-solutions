// Time Complexity: O(n)
// Space Complexity: O(1)

package main

func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	mostWater := 0

	for left < right {
		currWater := (right - left) * min(height[left], height[right])
		mostWater = max(mostWater, currWater)

		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return mostWater
}
