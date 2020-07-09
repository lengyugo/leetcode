"""
移动0
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        j  = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i > j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1
        return nums
from typing import List
"""
数组中未出现的数字
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        return [i+1 for i,num in enumerate(nums) if num > 0]

"""
数组中重复的数据
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            else:
                ans.append(num)
        return ans

"""
下一个排列
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        i = n-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0 and nums[i] == max(nums):
            return nums.reverse()
        else:
            j = n-1
            while j > i-1 and nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1],nums[j] = nums[j],nums[i-1]
            for k in range((n-i)//2):
                nums[i+k],nums[n-1-k] = nums[n-1-k],nums[i+k]

"""
排序数组中查找目标第一个和最后一个出现的位置
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def extedrime(nums, target, flag):
            left = 0
            right = len(nums)
            while left < right:
                mid = (right + left) // 2
                if nums[mid] > target or (flag and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left

        left_index = extedrime(nums, target, True)
        print(left_index)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, extedrime(nums, target, False) -1]

"""
寻找两个正序数组的中位数
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        m,n = len(nums1),len(nums2)
        left,right,ans = 0,m,-1
        midem1,midem2 = 0,0
        infinty = 2 **40
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums_im1 = (-infinty if i == 0 else nums1[i-1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j-1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                ans = i
                midem1,midem2 = max(nums_im1,nums_jm1),min(nums_i,nums_j)
                left = i+1
            else:
                right = i-1
        return (midem1 + midem2) / 2 if (m+n) % 2 == 0 else midem1

"""
顺时针打印矩阵
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            #print(list(zip(*matrix)))
            matrix = list(zip(*matrix))[::-1]
            #print(matrix)
        return res

"""
扑克牌中的数组
"""
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repet = set()
        ma,mi = 0,14
        for num in nums:
            if num == 0: continue
            ma = max(ma,num)
            mi = min(mi,num)
            if num in repet: return False
            repet.add(num)
        return ma - mi < 5

"""
最佳观光组合
"""
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        per_max = A[0] + 0
        for i in range(1,len(A)):
            ans = max(ans,per_max + A[i] - i)
            per_max = max(per_max,A[i] + i)
        return ans

"""
数字序列中的某一位数字
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        dight,start,count = 1,1,9
        while n > count:
            n -= count
            start *= 10
            dight += 1
            count = 9 * start * dight
        num = start + (n - 1) // dight
        return int(str(num)[(n-1)%dight])

"""
长度最小的子数组
"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        ans = n + 1
        start,end = 0,0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans,end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans== n + 1 else ans
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1]+nums[i])

        for i in range(1,n+1):
            target = s + sums[i-1]
            bound = bisect.bisect_left(sums,target)
            if bound != len(sums):
                ans = min(bound-i+1,ans)
        return 0 if ans== n + 1 else ans

"""
最长重复子数组
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxlength(addA, addB, length):
            res = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    res = max(res, k)
                else:
                    k = 0
            return res

        n, m = len(A), len(B)
        ans = 0
        for i in range(n):
            length = min(m, n - i)
            ans = max(ans, maxlength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ans = max(ans, maxlength(0, i, length))
        return ans

"""

合并两个有序数组
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1

        while p1 >=0 and p2 >=0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        print(nums1,nums2,p2)
        nums1[:p2+1] = nums2[:p2+1]