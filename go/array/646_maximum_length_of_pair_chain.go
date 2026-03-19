// Time Complexity: O(n log n)
// Space Complexity: O(1)
package main

import "sort"

func findLongestChain(pairs [][]int) int {
	if len(pairs) == 0 {
		return 0
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][1] < pairs[j][1]
	})

	count := 1
	currentEnd := pairs[0][1]

	for i := 1; i < len(pairs); i++ {
		if pairs[i][0] > currentEnd {
			count++
			currentEnd = pairs[i][1]
		}
	}

	return count
}
