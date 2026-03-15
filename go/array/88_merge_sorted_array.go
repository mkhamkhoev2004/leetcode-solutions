// Time Complexity: O(m + n)
// Space Complexity: O(1)
package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	m--
	n--
	i := len(nums1) - 1

	for n >= 0 {
		if m >= 0 && nums1[m] > nums2[n] {
			nums1[i] = nums1[m]
			m--
		} else {
			nums1[i] = nums2[n]
			n--
		}
		i--
	}
}
