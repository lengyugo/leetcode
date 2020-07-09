"""
最长公共前缀
"""
from typing import  List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[:i]
        return s1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        ss = list(map(set,zip(*strs)))
        print(ss)
        ans = ''
        for i,x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            ans += x[0]
        return ans


a = Solution()
print(a.longestCommonPrefix(["abb","aba","abac"]))