"""
最长公共子序列
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

"""
最长连续序列
"""
from typing import  List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_num = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                cur_long = 1

                while cur_num + 1 in nums_set:
                    cur_num +=1
                    cur_long += 1
                long_num = max(long_num,cur_long)
        return long_num


"""
最大正方形
"""
class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        maxque = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    maxque = max(maxque,dp[i][j])
        return maxque * maxque

"""
比特位计数
"""
from typing import  List
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1,num+1):
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp

"""
买卖股票含冷冻期
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0]*n for _ in range(3)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        dp[2][0] = 0

        for i in range(1,n):
            #第i天不持股
            dp[0][i] = max(dp[0][i-1],dp[2][i-1])
            #第i天持股
            dp[1][i] = max(dp[0][i-1]-prices[i],dp[1][i-1])
            #第i天冷冻期
            dp[2][i] = dp[1][i-1]+prices[i]
        return max(dp[0][n-1],dp[2][n-1])
"""
最长回文子串
"""
"""
中心扩散
"""
class Solution:
    def expendRoundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expendRoundCenter(s, i, i)
            left2, right2 = self.expendRoundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

"""动态规划"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and (s[i] == s[j]))

                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
                    print(ans)
            # print(dp)
        return ans
"""
分割等和子集
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        dp = [[False] * (target + 1) for _ in range(n)]
        dp[0][0] = True
        for i in range(1, target + 1):
            if i == nums[0]:
                dp[0][i] = True
                break

        for i in range(1, n):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


"""
最长有效括号
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2

                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                ans = max(ans, dp[i])
        return ans

"""
n个骰子的点数
"""
"""dp[i][j]表示扔完i次后，点数j出现的次数"""
class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [[0 for _ in range(6*n + 1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1,7):
                    if j >= k +1:
                        dp[i][j] += dp[i-1][j-k]
        ans = []

        for i in range(n,n*6+1):
            ans.append(dp[n][i] * 1.0 / 6**n)
        return ans

import collections
collections.Counter()

"""
一次编辑
"""
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False

        for i in range(min(m, n)):
            if first[i] != second[i]:
                return first[i + 1:] == second[i + 1:] or first[i:] == second[i + 1:] or first[i + 1:] == second[i:]
            else:
                pass
        return True

"""编辑距离"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        if m * n == 0:
            return m+n
        dp = [[0]*(n+1) for _ in range(m+1)]
        print(dp)
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        print(dp)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i][j-1]+1,
                        dp[i-1][j]+1,
                        dp[i-1][j-1]+1
                    )
        return dp[m][n]

"""
最长上升子序列
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)

        return max(dp)