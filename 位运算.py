"""
元音包含偶数次的最长字符串
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        char = {'a':0,'e':1,'i':2,'o':3,'u':4}
        find = {0:-1}
        val = 0
        ans = 0
        for i ,st in enumerate(s):
            if st in 'aeiou':
                val ^= (1 << (char[st]))
            if val not in find:
                find[val] = i
            else:
                ans = max(ans,i-find[val])
        return ans

"""
加法
"""
class Solution:
    def add(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.add(a^b,(a&b) << 1)

