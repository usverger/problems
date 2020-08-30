from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        for i in range(len(nums)):
            
            j = d.get(target - nums[i])
            if not j:
                continue
            
            if len(j) == 1:
                if (j[0] == i):
                    continue
                else:
                    return [i, j[0]]
            
            if len(j) > 1:
                if (j[0] == i):
                    return [i, j[1]]
                else:
                    return [i, j[0]]
            

