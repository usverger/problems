from typing import List
import sys
import bisect
from collections import defaultdict
from collections import Counter

class Solution:


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

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr: return False

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]: return True
        return False

    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        
        c = [0] * n
        c[0] = 1
        c[1] = 2
        for i in range(2, n):
            c[i] = c[i - 1] + c[i - 2]
        return c[n - 1]

    def climbStairsMinCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2: return sum(cost)
        
        total = [0] * n
        total[0] = cost[0]
        total[1] = cost[1]
        
        for i in range(2, n):
            total[i] = min(total[i - 1], total[i - 2]) + cost[i]
        
        return min(total[n - 1], total[n - 2])        

    def containsDuplicate(self, nums: List[int]) -> bool:
        s = list(sorted(nums))
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return True
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums == None or len(nums) <= 1: return False
        
        d = {}        
        right = 0
        
        while right < len(nums):
            if nums[right] in d:
                return True

            d[nums[right]] = right
            right += 1
            if right - k > 0:
                d.pop(nums[right - k - 1])
                
        return False

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

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == 0: continue
            
            index = nums[i] - 1
            while nums[index] != 0:
                newIndex = nums[index] - 1
                nums[index] = 0
                index = newIndex
                
        return [i + 1 for i in range(len(nums)) if nums[i] != 0]

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

    def firstBadVersion(self, n, isBadVersion):
        l = 1
        r = n
        while l < r:
            i =  l + (r - l) // 2
            if isBadVersion(i):
                r = i
            else:
                l = i + 1
            
        return l

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

    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        h = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != h[i]:
                counter += 1
        return counter

    def intersect_Counters(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # instead of searching and removing, calculate the counts and reduce the counters
        result = []
        c = Counter(nums2)

        for x in nums1:
            if c[x] > 0:
                c[x] -= 1
                result.append(x)
        return result
       
    def intersect_Naive(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # the naive - take one, look for each element in the second one
        # add the located number to the result array, removing it from the second
        # O(n^3) because removal also takes O(n)
        result = []
        for x in nums1:
            for y in nums2:
                if x == y:
                    nums2.remove(y)
                    result.append(x)
                    break
        return result

    def intersect_SortedSearch(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # following up Naive implementation
        # sort both, the do two pointers
        result = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

    def kSmallest(self, input, left, right, k) -> int:
        if (k - 1) < left: return -1
        if (k - 1) > right: return -1
        
        p = self.partition(input, left, right)
        if p == k - 1:
            return input[p]
        if p < k - 1:
            return self.kSmallest(input, p+1, right, k)
        else:
            return self.kSmallest(input, left, p-1, k)

    def maxSubArray_BruteForce(self, nums: List[int]) -> int:
        # naive brute force
        maximum = -2 ** 31
        for l in range(1, len(nums) + 1): # all possible lengths
            for i in range(len(nums) - l + 1): # all start elements of subarray while length allows
                maximum = max(sum(nums[i:i+l]), maximum)
        return maximum

    def maxSubArray_DP(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        for x in nums:
            currentSum = max(x, currentSum + x)
            maxSum = max(maxSum, currentSum)
        return maxSum

    def maxProfitManyTradesWithCooldown(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        # at t0:
        profitifsell = [0] * n
        profitifbuy = [0] * n
        profitifbuy[0] = -prices[0]
        
        for i in range(1, n):
            # on day i we can consider the following options:
            # if we held something, then we can either hold it or sell it
            # if we held nothing, then we can either buy something or do nothing
            profitifsell[i] = max(profitifsell[i - 1], profitifbuy[i - 1] + prices[i])
            profitifbuy[i] = max(profitifbuy[i - 1], profitifsell[i - 2] - prices[i])
        
        return max(profitifsell[n-1], profitifbuy[n-1])

    def maxProfitWithFee(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1: return 0

        # at t0:
        profitifsell = [0] * n
        profitifbuy = [0] * n
        profitifbuy[0] = -prices[0]
        
        for i in range(1, n):
            # on day i we can consider the following options:
            # if we held something, then we can either hold it or sell it
            # if we held nothing, then we can either buy something or do nothing
            profitifsell[i] = max(profitifsell[i - 1], profitifbuy[i - 1] + prices[i] - fee) # either do nothing or sell what we held
            profitifbuy[i] = max(profitifbuy[i - 1], profitifsell[i - 1] - prices[i])
            # looks like we get charged only at one side of the trade, this is not obvious from problem statement. Otherwise we need -fee on buying as well
        
        return max(profitifsell[n-1], profitifbuy[n-1])

    def maxProfitKTrades(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        profitifsell = [[0] * (k + 1)] * n
        profitifbuy = [[0] * (k + 1)] * n
        
        for t in range(1, k + 1):
            profitifbuy[0][t] = -prices[0]
        
        for i in range(1, n):
            for t in range(k, 0, -1):
                profitifsell[i][t] = max(profitifsell[i - 1][t], profitifbuy[i - 1][t] + prices[i])
                profitifbuy[i][t] = max(profitifbuy[i - 1][t], profitifsell[i - 1][t - 1] - prices[i])

        return max(profitifsell[n - 1])
        
    def maxProfitTwoTrades(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        profitifsell2 = [0] * n
        profitifbuy2 = [0] * n
        profitifsell1 = [0] * n
        profitifbuy1 = [0] * n
        
        profitifbuy1[0]= -prices[0]
        profitifbuy2[0]= -prices[0]
        
        for i in range(1, n):
            profitifsell2[i] = max(profitifsell2[i - 1], profitifbuy2[i - 1] + prices[i])
            profitifbuy2[i] = max(profitifbuy2[i - 1], profitifsell1[i - 1] - prices[i])
            profitifsell1[i] = max(profitifsell1[i - 1], profitifbuy1[i - 1] + prices[i])
            profitifbuy1[i] = max(profitifbuy1[i - 1], -prices[i])

        return profitifsell2[n - 1]

    def maxProfitOneTrade(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        # at t0:
        profitifsell = [0] * n
        profitifbuy = [0] * n
        profitifbuy[0] = -prices[0]
        
        for i in range(1, n):
            # on day i we can consider the following options:
            # if we held something, then we can either hold it or sell it
            # if we held nothing, then we can either buy something or do nothing
            profitifsell[i] = max(profitifsell[i - 1], profitifbuy[i - 1] + prices[i])
            profitifbuy[i] = max(profitifbuy[i - 1], -prices[i])
        
        return max(profitifsell[n-1], profitifbuy[n-1])

    def maxProfitManyTrades(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        # at t0:
        profitifsell = [0] * n
        profitifbuy = [0] * n
        profitifbuy[0] = -prices[0]
        
        for i in range(1, n):
            # on day i we can consider the following options:
            # if we held something, then we can either hold it or sell it
            # if we held nothing, then we can either buy something or do nothing
            profitifsell[i] = max(profitifsell[i - 1], profitifbuy[i - 1] + prices[i])
            profitifbuy[i] = max(profitifbuy[i - 1], profitifsell[i - 1] - prices[i])
        
        return max(profitifsell[n-1], profitifbuy[n-1])

    def mergeSort(self, nums: List[int]):

        if len(nums) > 1:
            center = len(nums) // 2
            a = nums[:center]
            b = nums[center:]
            self.mergeSort(a)
            self.mergeSort(b)
            self.mergeSortedIntoNew(nums, a, b)

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

    def mergeSortedIntoNew(self, nums: List[int], a: List[int], b: List[int]) -> None:
        i = 0
        j = 0
        for k in range(0, len(nums)):
            if (i < len(a) and j < len(b) and a[i] <= b[j]) or j > len(b) - 1:
                nums[k] = a[i]
                i += 1
            elif (i < len(a) and j < len(b) and a[i] > b[j]) or i > len(a) - 1:
                nums[k] = b[j]
                j += 1

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

    def minSubArrayLen_BruteForce(self, s: int, nums: List[int]) -> int:
       for l in range(1, len(nums) + 1): # all possible lengths
           for i in range(len(nums) - l + 1): # all possible subarrays of given length
               m = sum(nums[i:i+l])
               if m >= s:
                   return l
               
       return 0

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

    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivot = nums[r]
        slow = l
        for fast in range(l,r):
            if nums[fast] < pivot:
                temp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = temp
                slow += 1
        nums[r] = nums[slow]
        nums[slow] = pivot
        return slow

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
 
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 >= 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        digits.insert(0, 1)
        return digits

    def quickSort(self, input, left, right):
        if left < right:
            p = self.partition(input, left, right)
            self.quickSort(input, left, p-1)
            self.quickSort(input, p+1, right)

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

    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: return arr
        if len(arr) == 1:
            arr[0] = -1
            return arr
        
        i = len(arr) - 2
        m = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            m = max(m, temp)
            i -= 1
        return arr

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return sum(nums)
        if n == 2: return max(nums[0], nums[1])
        
        profit = [0] * n
        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            profit[i] = max(profit[i - 1], profit[i - 2] + nums[i])
            
        return profit[n - 1]

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

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0 # left pointer for even numbers
        j = len(A) - 1 # right pointer for odd numbers
        while i < j:
            while i < j and A[i] % 2 == 0: i += 1 # skip all even numbers
            while i < j and A[j] % 2 == 1: j -= 1 # skip all odd numbers
            
            if i < j:
                t = A[i]
                A[i] = A[j]
                A[j] = t
        
        return A        

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

    def sumOddLengthSubarrays_BruteForce(self, arr: List[int]) -> int:
        
        result = 0
        for l in range(1, len(arr) + 1, 2): # iterate over all odd lengths
            for i in range(0, len(arr) - l + 1):
                result += sum(arr[i:i + l])
        
        return result

    def thirdMax(self, nums: List[int]) -> int:
        m1 = max(nums) # O(n)
        
        f = list(filter(lambda x: x != m1, nums))
        if not f: return m1
        m2 = max(f) # O(n)
        
        f = list(filter(lambda x: x != m1 and x != m2, nums))
        if not f: return m1
        m3 = max(f)
        
        return m3

    def thirdMax2(self, nums: List[int]) -> int:
        if not nums: return -sys.maxsize - 1
        max = -sys.maxsize - 1
        max2 = -sys.maxsize - 1
        max3 = -sys.maxsize - 1
        for i in range(0, len(nums)):
            if nums[i] > max:
                max3 = max2
                max2 = max
                max = nums[i]
            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] > max3:
                max3 = nums[i]
        return max3

    def thirdMin(self, nums: List[int]) -> int:
        if not nums: return sys.maxsize
        min = sys.maxsize
        min2 = sys.maxsize
        min3 = sys.maxsize
        for i in range(0, len(nums)):
            if nums[i] < min:
                min3 = min2
                min2 = min
                min = nums[i]
            elif nums[i] < min2:
                min3 = min2
                min2 = nums[i]
            elif nums[i] < min3:
                min3 = nums[i]
        return min3

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

    def validMountainArray(self, A: List[int]) -> bool:
        if not A: return False
        if len(A) < 3: return False

        i = 0
        while i < len(A) - 1 and A[i] < A[i + 1]: i +=1 # climb the left slope
        if i == 0: return False # there was no climb at all - this is not mountain

        j = len(A) - 1
        while j > 0 and A[j] < A[j - 1]: j -=1 # climb the right slope
        if j == len(A) - 1: return False # there was no climb at all - this is not mountain

        # the peak is the one
        return i == j
