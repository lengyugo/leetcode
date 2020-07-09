"""
分割链表
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next

"""
相交链表
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha = headA
        hb = headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

"""
环形链表 
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        quick, slow = head, head
        while quick and slow:
            slow = slow.next
            if quick.next:
                quick = quick.next.next
            else:
                return False

            if quick is slow:
                return True
        return False

"""
环形链表2
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast,slow = head,head
        while True:
            if not (fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast,slow = fast.next,slow.next
        return fast
"""
回文串链表
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        ##反转
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        p1 = head
        p2 = prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

"""
删除链表第k个节点
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        length = 0
        first = head
        dummy.next = head
        while first:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next


"""
链表求和
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        cur = res
        tmp = 0
        while l1 and l2:
            s = l1.val + l2.val + tmp
            l1.val = s % 10
            tmp = s // 10
            cur.next = l1
            cur = cur.next
            l1, l2 = l1.next, l2.next

        left = None
        if l1:
            left = l1
        else:
            left = l2

        while left and tmp >= 0:
            s = left.val + tmp
            left.val = s % 10
            tmp = s // 10
            cur.next = left
            cur = cur.next
            left = left.next
        if tmp > 0:
            cur.next = ListNode(tmp)
        return res.next
