// Time Complexity: O(n^2)
// Space Complexity: O(n^2)
package main

func generate(numRows int) [][]int {
	var ans [][]int

	for i := 0; i < numRows; i++ {
		if i == 0 {
			ans = append(ans, []int{1})
			continue
		}
		if i == 1 {
			ans = append(ans, []int{1, 1})
			continue
		}

		row := make([]int, i+1)
		row[0] = 1
		row[len(row)-1] = 1
		lastRow := ans[len(ans)-1]

		for j := 1; j < len(row)-1; j++ {
			row[j] = lastRow[j-1] + lastRow[j]
		}
		ans = append(ans, row)
	}

	return ans
}
