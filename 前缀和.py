"""
和可被K整除的子数组
"""
from typing import  List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0:1}
        ans,total = 0,0
        for num in A:
            total += num
            model = total % K
            print(model)
            same = record.get(model,0)
            print(same)
            ans += same
            print(ans)
            record[model] = same + 1
            print("************")
        return ans

