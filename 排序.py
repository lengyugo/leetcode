"""
把数组排成最小的数
"""
import functools
class Solution:
    def minNumber(self, nums) -> str:
        def sort_rule(x,y):
            a,b = x, y
            if a + b > b + a:
                return 1
            elif a+b < b+a:
                return -1
            else:
                return 0
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)
"""
堆
"""
import heapq
from typing import List

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k > len(arr) or k == 0:
            return []
        heap = []
        for i in arr[:k]:
            heapq.heappush(heap, -i)
        #print(heap)
        for i in arr[k:]:
            if i < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -i)
                #print(heap)
        ans = []
        for i in range(k):
            ans.append(-heapq.heappop(heap))
        return ans[::-1]

a = Solution()
print(a.smallestK([1,3,5,7,2,4,6,8],4))


"""
数组中的第k大元素
"""
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(left, right, nums):
            l, r = left, right
            index = random.randint(l, r)
            nums[l], nums[index] = nums[index], nums[l]
            while l < r:
                while l < r:
                    if nums[r] < nums[l]:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        while l < r:
                            if nums[l] > nums[r]:
                                nums[l], nums[r] = nums[r], nums[l]
                                r -= 1
                                break
                            else:
                                l += 1
                    else:
                        r -= 1

            if l == len(nums) - k:
                return nums[l]
            elif l > len(nums) - k:
                return quick_sort(left, l - 1, nums)
            else:
                return quick_sort(l + 1, right, nums)

        return quick_sort(0, len(nums) - 1, nums)
