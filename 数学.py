"""
圆圈中最后剩下的数字
"""
import sys
sys.setrecursionlimit(100000)
class Solution:
    def f(self,n,m):
        if n == 0: return 0
        x = self.f(n-1,m)
        return (m+x)% n
    def lastRemaining(self, n: int, m: int) -> int:
        return self.f(n,m)

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2,n+1):
            f = (m+f) % i
        return f