# Time Complexity: O(log N)
# Space Complexity: O(log N)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit**2 for digit in str(n)))

        return n == 1