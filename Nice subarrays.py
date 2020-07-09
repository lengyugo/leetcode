"""
暴力
"""
def numberOfSubarrays(nums, k: int) -> int:
    left, right = 0, 0
    if not nums:
        return 0

    def count(nums):
        count = 0
        for num in nums:
            if num % 2 != 0:
                count += 1
        return count

    if count(nums) < k or count(nums) == 0:
        return 0
    #print(count([1,2,1,1]))
    ans = 0
    for i in range(len(nums)):
        left = i
        for j in range(i+1, len(nums)):
            # print(j)
            # print(nums[i:j+1])
            if count(nums[left:j+1]) == k:
                # right = j + 1
                # ans.append(nums[left:right])
                ans += 1


    return ans
"""

"""

def numberOfSubarrays1( nums, k: int) -> int:
    n = len(nums)
    odd = [-1]
    ans = 0
    for i in range(n):
        if nums[i] % 2 == 1:
            odd.append(i)
    odd.append(n)
    print(odd)
    for i in range(1, len(odd) - k):

        ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
    return ans

"""

"""
def numberOfSubarrays2( nums ,k: int) -> int:
    cnt = [0] * (len(nums) + 1)
    cnt[0] = 1
    odd, ans = 0, 0
    for num in nums:
        if num % 2 == 1:
            odd += 1
        if odd >= k:
            ans += cnt[odd - k]
        cnt[odd] += 1

    return ans

a = numberOfSubarrays1([1,1,2,1,1],3)
print(a)
