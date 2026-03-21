# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        most_water = 0
        
        while left < right:
            curr_water = (right - left) * min(height[left], height[right])
            most_water = max(most_water, curr_water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return most_water