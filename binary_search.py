"""
最大宽度坡
"""
def maxWidthRamp( A) -> int:
    ans = 0
    m = float('inf')
    for i in sorted(range(len(A)), key=A.__getitem__):
        #print(i)
        ans = max(ans, i - m)
        #print(ans)
        m = min(m, i)
        #print(m)

    return ans
"""
单调栈
"""


def maxWidthRamp1( A) -> int:
    stack = []
    n = len(A)
    for i in range(n):
        if not stack or A[stack[-1]] > A[i]:
            stack.append(i)
    print(stack)
    res = 0
    i = n - 1
    while i > res:  # 当res大于等于i时没必要继续遍历了
        while stack and A[stack[-1]] <= A[i]:
            res = max(res, i - stack[-1])
            stack.pop()
            #print(stack)
        i -= 1

    return res

"""
二叉搜索树和双向链表
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if self.per:
                self.per.right,cur.left = cur,self.per
            else:
                self.head = cur

            self.per = cur
            dfs(cur.right)

        if not root: return None
        self.per = None
        dfs(root)
        self.head.left,self.per.right = self.per,self.head
        return self.head


"""
前序和中序遍历构造二叉树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1],inorder[:i])
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root
"""
从中序和后续遍历构造二叉树
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i+1:],postorder[i:-1])
        return root















