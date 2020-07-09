"""

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) :
        right_most_val = dict()
        max_depth = -1
        queue = deque([(root,0)])
        while queue:
            node,depth = queue.popleft()

            if node is not None:
                max_depth = max(depth,max_depth)

                right_most_val[depth] = node.val
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))

        return [right_most_val[dep] for dep in range(max_depth+1)]
"""

"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.next and cur.right: cur.right.next = cur.next.left

                cur = cur.next
            pre = pre.left
        return root

"""
二叉树变为累加树
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return []
        if root.right:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        else:
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

"""
对称二叉树-递归
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left,node2.right) and check(node1.right,node2.left)
        return check(root,root)

"""
对称二叉树-迭代
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            queue = next_queue
        return True

"""
二叉树的直径
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(root):
            if not root: return 0
            l = depth(root.left)
            r = depth(root.right)
            self.ans = max(self.ans,l+r)
            return max(l,r) + 1

        depth(root)
        return self.ans

"""
二叉树转化为链表
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

"""
二叉树的最大路径和
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            nonlocal ans
            if not node: return 0
            sum_left = max(helper(node.left), 0)
            sum_right = max(helper(node.right), 0)
            path = sum_left + sum_right + node.val
            ans = max(ans, path)
            return max(sum_right, sum_left) + node.val

        ans = float('-inf')
        helper(root)
        return ans

"""
平衡二叉树
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

"""
二叉树的序列化和反序列化
"""
import  collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return '[]'
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            node = queue.popleft()
            if node:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append('null')
        return '[' + ','.join(ans) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        visits, i = data[1:-1].split(','), 1
        queue = collections.deque()
        root = TreeNode(int(visits[0]))
        queue.append(root)
        while queue:
            node = queue.popleft()
            if visits[i] != 'null':
                node.left = TreeNode(int(visits[i]))
                queue.append(node.left)

            i += 1
            if visits[i] != 'null':
                node.right = TreeNode(int(visits[i]))
                queue.append(node.right)
            i += 1
        return root

"""
从先序遍历还原二叉树
"""
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path,pos = list(),0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ans = {-1: TreeNode(0)}

        def addtree(v, p):
            ans[p] = TreeNode(int(v))
            if not ans[p - 1].left:
                ans[p - 1].left = ans[p]
            else:
                ans[p - 1].right = ans[p]

        val, path = '', 0
        for c in S:
            if c != '-':
                val += c
            elif val:
                addtree(val, path)
                val, path = '', 1
            else:
                path += 1
        addtree(val, path)
        return ans[0]