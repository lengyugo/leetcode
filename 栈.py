"""
每日温度
"""
class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * (len(T))
        stack = []
        for i in range(len(T)-1,-1,-1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

"""
下一个更大的元素
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        hashmap = dict()
        for i in nums2:
            while len(ans) != 0 and ans[-1] < i: hashmap[ans.pop()]= i
            ans.append(i)
        return [hashmap.get(i,-1)for i in nums1]


"""
下一个更大的元素2
"""
class Solution:
    def nextGreaterElements(self, nums) :
        stack = []
        l = len(nums)
        ans = [-1] * l

        for i in range(2*l-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i % l]:
                stack.pop()
            ans[i % l] = -1 if stack == [] else nums[stack[-1]]
            stack.append(i % l)
        return ans

"""
链表中下一个最大元素
单调栈
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) :
        stack = []
        stack_loc = []
        loc = -1
        ans = []
        while head:
            loc += 1
            ans.append(0)
            while stack and stack[-1] < head.val:
                ans[stack_loc[-1]] = head.val
                stack.pop()
                stack_loc.pop()

            stack.append(head.val)
            stack_loc.append(loc)

            head = head.next
        return ans

"""
最长有效括号
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans,i-stack[-1])
        return ans

"""
二叉树的后序遍历序列
"""
from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack,root = [],float('inf')
        for i in range(len(postorder)-1,-1,-1):
            if postorder[i] > root: return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True