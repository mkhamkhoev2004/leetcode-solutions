# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start = 0
        max_len = 1
        
        def growPalindrome(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    max_len = curr_len
                    start = left
                left -= 1
                right += 1
        
        for i in range(len(s)):

            growPalindrome(i, i)
            
            growPalindrome(i, i + 1)
        
        return s[start:start + max_len]