"""
和为s的两个数字
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums) -1
        while i < j:
            s = nums[i] + nums[j]
            if s < target: i += 1
            elif s > target: j -= 1
            else: return nums[i],nums[j]
        return []

"""
删除链表中的节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        per,cur = head,head.next
        while cur and cur.val != val:
            per,cur = cur,cur.next
        if cur:
            per.next = cur.next
        return head