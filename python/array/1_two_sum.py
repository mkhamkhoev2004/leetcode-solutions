# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(nums, target):
    m = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in m:
            return [m[complement], i]
        m[num] = i
    return None
