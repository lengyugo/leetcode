"""
朋友圈
"""
class Solution:
    def findCircleNum(self, M) -> int:
        n = len(M)
        ans = n
        p = [[i] for i in range(n)]
        for i in range(n):

            for j in range(i,n):

                if M[i][j] == 1 and p[i] is not p[j]:
                    p[i] += p[j]

                    for k in p[j]:
                        p[k]= p[i]

                    ans -= 1
        return ans

A = Solution()
print(A.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

"""
等式方程的可满足性
"""
class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for st in equations:
            if st[1] == '=':
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                uf.union(index1, index2)

        for st in equations:
            if st[1] == '!':
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')

                if uf.find(index1) == uf.find(index2):
                    return False
        return True