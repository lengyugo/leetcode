"""
找到字符串中所有字母的异位词
"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m,n = len(s),len(p)
        left,right = 0,0
        needs = dict((i,p.count(i)) for i in p)
        window = {}
        size = 0
        ans = []
        while right < m:
            c1 = s[right]
            if c1 in needs.keys():
                window[c1]  = window.get(c1,0) + 1
                if window[c1] == needs[c1]:
                    size += 1
            right += 1
            while right - left >= n:
                if size == len(needs):
                    ans.append(left)
                c2 = s[left]
                if c2 in needs.keys():
                    if window[c2] == needs[c2]:
                        size -= 1
                    window[c2] -= 1
                left += 1
        return ans

"""
滑动窗口的最大值
"""
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        queue = collections.deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]: queue.pop()
            queue.append(nums[i])

        ans = [queue[0]]
        for i in range(k, len(nums)):
            if queue[0] == nums[i - k]: queue.popleft()
            while queue and queue[-1] < nums[i]: queue.pop()
            queue.append(nums[i])
            ans.append(queue[0])
        return ans

"""
最长不含重复字符的子字符串
"""
"哈希表+双指针"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic,ans,i = {},0,-1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]],i)
            dic[s[j]] = j
            ans = max(ans,j-i)
            print(ans)
        return ans
"动态规划+哈希表"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ans = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j],-1)
            dic[s[j]] = j
            tmp = tmp + 1 if tmp < j -i else j-i
            ans = max(ans,tmp)
        return ans