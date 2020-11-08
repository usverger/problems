from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.nums, key = lambda x: random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

    def __init__(self):
        self.l = []
        
    def push(self, x: int) -> None:
        if self.l:
            m = self.l[-1][1]
            self.l.append([x, min(x,m)])
        else:
            self.l.append([x, x])

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        return self.l[-1][1]