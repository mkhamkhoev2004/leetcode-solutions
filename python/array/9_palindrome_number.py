# Time Complexity: O(n)
# Space complexity: O(1)
# I consider n as the number
# of digits in the x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x%10 == 0 and x != 0 or x < 0:
            return False
        
        reversed = 0
        while x > reversed:
            reversed = reversed * 10  + x % 10
            x //= 10

        return x == reversed or x == reversed // 10