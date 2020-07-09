import bisect
"""
数组中的逆序对
"""
class Solution:
    def reversePairs(self, nums) -> int:
        ans,t = 0,[]
        for i,v in enumerate(nums):
            index = bisect.bisect(t,v)
            print(index)
            ans += i - index
            print(ans)
            bisect.insort(t,v)
            print(t)
        return ans














"""
排序链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        mid, slow.next = slow.next, None
        p = res = ListNode(0)
        left, right = self.sortList(head), self.sortList(mid)
        while left and right:
            if left.val < right.val:
                p.next, left = left, left.next
            else:
                p.next, right = right, right.next
            p = p.next
        p.next = left if left else right
        return res.next






















A = Solution()
A.reversePairs([7,5,6,4])
print(A)