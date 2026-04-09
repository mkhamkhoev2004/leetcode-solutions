# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        r = 0
        max_len = 0

        while r < len(s):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1

            my_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len