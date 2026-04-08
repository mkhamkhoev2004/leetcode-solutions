# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        # steps = [0] * (n + 1)
        # steps[1] = 1
        # steps[2] = 2

        # for i in range(3, n + 1):
        #     steps[i] = steps[i - 1] + steps[i - 2]

        # return steps[n]

        prev1 = 1
        prev2 = 2

        for i in range(3, n + 1):
            prev1, prev2 = prev2, prev1 + prev2
        
        return prev2