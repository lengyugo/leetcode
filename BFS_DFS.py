"""
从上到下打印二叉树3
"""
import collections
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root: return []
        ans,queue = [],collections.deque()
        queue.append(root)
        while queue:
            tmp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(ans) % 2:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if  node.left: queue.append(node.left)
                if  node.right: queue.append(node.right)
            ans.append(list(tmp))
        return ans


"""
朋友圈
"""
class Solution:
    def findCircleNum(self, M) -> int:
        n = len(M)
        visited = [0] * n
        ans = 0
        queue = []
        for i in range(n):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    s = queue.pop()
                    visited[s] = 1
                    for j in range(n):
                        if M[s][j] == 1 and visited[j] == 0:
                            queue.append(j)
                ans += 1
        return ans

"""
二叉树中和为某一值的路径
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        ans, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                ans.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum_)
        return ans


"""
除法求值
先建图，在dfs
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        def dfs(s, t):
            if s not in graph:
                return -1
            if s == t:
                return 1

            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        ans = []
        for ds, dt in queries:
            visited = set()
            ans.append(dfs(ds, dt))
        return ans

"""
课程表
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for cur,per in prerequisites:
            ind[cur] += 1
            adj[per].append(cur)
        print(ind,adj)
        q = collections.deque()
        for i in range(len(ind)):
            if not ind[i]: q.append(i)
        print(q)
        while q:
            per = q.popleft()
            numCourses -= 1
            for cur in adj[per]:
                ind[cur] -= 1
                #print(ind[cur])
                if not ind[cur]: q.append(cur)
        return not numCourses

"""
课程表2
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        inges = [0] * numCourses
        ans = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            inges[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if inges[u]==0])

        while q:
            u = q.popleft()
            ans.append(u)
            for v in edges[u]:
                inges[v] -= 1
                if inges[v] == 0:
                    q.append(v)

        if len(ans) != numCourses:
            ans = list()
        return ans

"""
字符串解码
"""
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s,i):
            ans,mutil = '', 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    mutil = mutil * 10 + int(s[i])
                    #print(mutil)
                elif s[i] == '[':
                    i,tmp = dfs(s,i+1)
                    ans += mutil * tmp
                    print(ans)
                    mutil = 0
                elif s[i] == ']':
                    return i,ans
                else:
                    ans += s[i]
                i+=1
            return ans
        return dfs(s,0)
"""
字符串解码
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack,mutli,ans = [],0,''
        for c in s:
            if c == '[':
                stack.append([mutli,ans])
                mutli,ans = 0,''
            elif c == ']':
                cur_mutli,last_ans = stack.pop()
                ans = last_ans + cur_mutli * ans
            elif '0' <= c <= '9':
                mutli = mutli * 10 + int(c)
            else:
                ans += c
        return ans

"""
删除无效括号
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValued(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0: return False
            return cnt == 0

        level = {s}
        while True:
            print(level)
            vailued = list(filter(isValued, level))
            print(vailued)
            if vailued: return vailued
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level

"""
单词接龙
"""
from collections import  defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        all_word = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                all_word[word[:i]+'-'+word[i+1:]].append(word)
        print(all_word)
        queue = [(beginWord,1)]
        visited = {beginWord:True}
        while queue:
            cur_word,level = queue.pop(0)
            for i in range(len(beginWord)):
                match = cur_word[:i] + '-' + cur_word[i+1:]
                for word in all_word[match]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word,level+1))
                all_word[match] = []
        return 0

"""
单词接龙2
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)

        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '-' + word[i + 1:]
                buckets[match].append(word)
        # print(buckets)
        preWords = defaultdict(list)
        toSeen = deque([(beginWord, 1)])
        beFound = {beginWord: 1}
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '-' + curWord[i + 1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level + 1
                        toSeen.append((word, level + 1))

                    if beFound[word] == level + 1:
                        preWords[word].append(curWord)
            if endWord in beFound and level + 1 > beFound[endWord]:
                break
        # print(preWords)
        if endWord in beFound:
            ans = [[endWord]]
            while ans[0][0] != beginWord:
                ans = [[word] + r for r in ans for word in preWords[r[0]]]
                print(ans)
            return ans
        else:
            return []
"""
矩阵中的路径
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            if not 0 <= i < len(board) or not 0<= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) -1: return True
            tmp,board[i][j] = board[i][j],'/'
            ans = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            board[i][j] = tmp
            return ans
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): return True
        return False