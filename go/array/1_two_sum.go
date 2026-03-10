// Time Complexity: O(n)
// Space Complexity: O(n)
package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		if idx, ok := m[target-num]; ok {
			return []int{idx, i}
		}
		m[num] = i
	}
	return nil
}
