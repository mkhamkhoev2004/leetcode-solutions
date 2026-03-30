# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(numRows):
            if i == 0:
                ans.append([1])
                continue
            if i == 1:
                ans.append([1, 1])
                continue
            
            row = [0] * (i + 1)
            row[0] = 1
            row[-1] = 1
            last_row = ans[-1]
            
            for j in range(1, len(row) - 1):
                row[j] = last_row[j-1] + last_row[j]
            
            ans.append(row)
        
        return ans