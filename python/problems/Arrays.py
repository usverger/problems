from typing import List
from collections import defaultdict

class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr: return False

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]: return True
        return False

    def mergeSorted(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1 # pointer of the new arr
        i = m - 1 # pointer on nums1
        j = n - 1 # pointer on nums2
        while k >= 0:            
            if (i >= 0 and j >= 0 and nums1[i] >= nums2[j]) or j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif (i >= 0 and j >= 0 and nums1[i] < nums2[j]) or i < 0:
                nums1[k] = nums2[j]
                j -= 1           
            
            k -= 1

    def duplicateZeros(self, arr: List[int]) -> None:
        
        def shiftRight(index: int, arr: List[int]):
            i = len(arr) - 1
            while i > index:
                arr[i] = arr[i - 1]
                i -= 1
            arr[index] = 0
        
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                shiftRight(i + 1, arr)
                i += 1
            i += 1

    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [0]*len(A) # declare an array of known length
        i = 0 # left pointer
        j = len(A) - 1 # right pointer
        k = len(result) - 1 # result pointer
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                result[k] = A[i]**2
                i += 1
            else:
                result[k] = A[j]**2
                j -= 1

            k -= 1
        return result
        
    def findNumbers(self, nums: List[int]) -> int:
        
        def digits(n: int) -> int:
            d = 0
            while n // 10 > 0:
                d += 1
                n = n // 10
            return d + 1
        
        c = 0 # counter
        for i in range(len(nums)):
            d = digits(nums[i])
            if d % 2 == 0:
                c += 1
        return c

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        i = 1 # slow pointer to show the end of result array
        j = 1 # fast pointer
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i - 1]: j +=1 # skip duplicate values
            if j < len(nums):
                nums[i] = nums[j]
                i += 1
                j += 1
        return i

    def getPascalRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        
        # prepare the result
        a = [0] * (rowIndex + 1)
        a[0] = 1
        
        for _ in range(1, rowIndex + 1):
            a[0] = 1
            prev = a[0]
            for i in range(1, len(a)):
                new = a[i] + prev
                prev = a[i]
                a[i] = new
        return a

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        start = 0
        count = 0
        while count < n:
            currentIndex = start
            currentValue = nums[start]
            while True: # start the stepping and remember the the current value
                nextIndex = (currentIndex + k) % n
                temp = nums[nextIndex]
                nums[nextIndex] = currentValue
                currentValue = temp
                currentIndex = nextIndex
                count += 1
                
                if start == currentIndex:
                    break
            start += 1
        
        #extra array to hold the right part
        #right = nums[-k:]
        #for i in reversed(range(n - k)):
        #    nums[i + k] = nums[i]
        #for i in range(len(right)):
        #    nums[i] = right[i]
            
        #brute force - k times rotate by 1   
        #for s in range(k):
        #    last = nums[-1]
        #    for i in range(n - 1):
        #        temp = last
        #        last = nums[i]
        #        nums[i] = temp

    def minSubArrayLen_BruteForce(self, s: int, nums: List[int]) -> int:
       for l in range(1, len(nums) + 1): # all possible lengths
           for i in range(len(nums) - l + 1): # all possible subarrays of given length
               m = sum(nums[i:i+l])
               if m >= s:
                   return l
               
       return 0
    
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        m = 2**31 - 1
        currentSum = 0
        for i in range(len(nums)): # expand the right bracket
            currentSum += nums[i]
            while currentSum >= s: # found a sub array candidate, try shrinking the left bracket
                m = min(m, i - left + 1) 
                currentSum -= nums[left]
                left += 1
        return m if m < 2**31 - 1 else 0

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0 # counter of ones
        m = 0 # maximum counter of ones
        for i in nums:
            if i == 1:
                c += 1
                m = max(m, c)
            else:
                c = 0

        return m

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
                
            
                
        
                
                
            

