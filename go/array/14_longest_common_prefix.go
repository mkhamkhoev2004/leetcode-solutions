// Time Complexity: O(n)
// Space Complexity: O(n)
package main

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	for i, letter := range strs[0] {
		for _, word := range strs {
			if i >= len(word) || rune(word[i]) != letter {
				return strs[0][:i]
			}
		}
	}
	return strs[0]
}
