from typing import List
from collections import defaultdict

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def twoSumSorted(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]
            
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

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
            

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    def addBinary(self, a: str, b: str) -> str:
        #aint = int(a, 2)
        #bint = int(b, 2)
        #return bin(aint + bint)[2:]
        
        result = ''
        carry = 0
        length = max(len(a), len(b))
        
        for i in range(1, length + 1):
            adigit = int(a[-i]) if i <= len(a) else 0
            bdigit = int(b[-i]) if i <= len(b) else 0
            rdigit = (adigit + bdigit + carry) % 2
            carry = 1 if (adigit + bdigit + carry) > 1 else 0
            
            result = str(rdigit) + result
            
        if carry == 1:
            result = '1' + result
            
        return result

    def addStrings(self, num1: str, num2: str) -> str:
        
        if len(num1) < len(num2):
            shorter = num1
            longer = num2
        else:
            shorter = num2
            longer = num1

        result = str('')
        carry = 0
        i = 0
        while i < len(shorter):
            a = shorter[len(shorter) - 1 - i]
            b = longer[len(longer) - 1 - i]
            c = (int(a) + int(b) + carry) % 10
            carry = (int(a) + int(b) + carry) // 10
            result = str(c) + result
            i += 1
        
        while i < len(longer):
            b = longer[len(longer) - 1 - i]
            c = (int(b) + carry) % 10
            carry = (int(b) + carry) // 10
            result = str(c) + result
            i += 1
            
        if carry == 1:
            result = '1' + result
            
        return result

    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 >= 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        digits.insert(0, 1)
        return digits

    def dominantIndex(self, nums: List[int]) -> int:
        max = 0
        maxIndex = -1
        for i, v in enumerate(nums):
            if v > max:
                maxIndex = i
                max = v
                
        for i, v in enumerate(nums):
            if 2*v > max and i != maxIndex:
                return -1
            
        return maxIndex

    def sumOddLengthSubarrays_BruteForce(self, arr: List[int]) -> int:
        
        result = 0
        for l in range(1, len(arr) + 1, 2): # iterate over all odd lengths
            for i in range(0, len(arr) - l + 1):
                result += sum(arr[i:i + l])
        
        return result

    def moveZeroes(self, nums: List[int]) -> None:
        
        def swap(i: int, j: int, nums: List[int]):
            k = nums[j]
            nums[j] = nums[i]
            nums[i] = k
        
        last = 0
        for i in range(len(nums)):          
            if nums[i] != 0:
                swap(i, last, nums)
                last += 1

    def pivotIndex(self, nums: List[int]) -> int:
        
        # corner case when list is empty
        if len(nums) == 0:
            return -1
        
        total = sum(nums)

        # check leftmost element since it is not part of the cycle
        if total - nums[0] == 0:
            return 0
        
        leftSum = 0
        rightSum = total - nums[0]
        
        for i in range(1, len(nums)):
            leftSum += nums[i - 1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        
        return -1
                    
    def numIdenticalPairs_BruteForce(self, nums: List[int]) -> int:
        
        def good(i: int, j: int, nums: List[int]) -> bool:
            return nums[i] == nums[j] and i < j
        
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if good(i, j, nums):
                    count += 1
        return count
                                  
    def numIdenticalPairs_Linear(self, nums: List[int]) -> int:

        histogram = [0] * 100 # according to problem statement

        for value in nums:
            histogram[value] += 1

        result = 0
        for count in histogram:
            # C of n elements by k = n! / (k! * (n - k)!)
            # in our case count! / (2! * (count - 2)!) = count * (count - 1) / 2
            result += count * (count - 1) // 2

        return result
                
            
                
        
                
                
            

