# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        for i, letter in enumerate(strs[0]):
            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return strs[0][:i]
        return strs[0]