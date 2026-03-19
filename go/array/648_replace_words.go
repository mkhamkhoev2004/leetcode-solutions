// Time Complexity: O(n * m)
// Space Complexity: O(d + n)
package main

import "strings"

func replaceWords(dictionary []string, sentence string) string {
	rootSet := make(map[string]bool)
	for _, root := range dictionary {
		rootSet[root] = true
	}

	words := strings.Fields(sentence)

	for i, word := range words {
		for j := 1; j <= len(word); j++ {
			prefix := word[:j]

			if rootSet[prefix] {
				words[i] = prefix
				break
			}
		}
	}

	return strings.Join(words, " ")
}
