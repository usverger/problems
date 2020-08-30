from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]
            
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
