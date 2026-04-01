# Time Complexity: O(4^n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def build(curr, open_count, close_count):

            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            if open_count < n:
                build(curr + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                build(curr + ')', open_count, close_count + 1)

        build("", 0, 0)
        return result