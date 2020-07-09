"""
幂集
"""
class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(nums, path, res):
            res.append(path)
            if nums == []:
                return []
            for i in range(len(nums)):
                backtrack(nums[i + 1:], path + [nums[i]], res)

        backtrack(nums, [], result)

        return result

"""
组合
"""


def combine( n: int, k: int) :
    def backtrack(first=1, cur=[]):
        if len(cur) == k:
            output.append(cur[:])

        for i in range(first, n + 1):
            cur.append(i)
            backtrack(i + 1, cur)
            cur.pop()

    output = []
    backtrack()
    return output

"""
八皇后
"""
board_size = 8
solution_count = 0
queen_list = [0] * board_size

def eight_queens(cur_column):
    if cur_column >= board_size:
        global solution_count
        solution_count += 1
        print(queen_list)
    else:
        for i in range(board_size):
            if is_vaild_pos(cur_column,i):
                queen_list[cur_column] = i
                eight_queens(cur_column+1)

def is_vaild_pos(cur_column,pos):
    i = 0
    while i < cur_column:
        if queen_list[i] == pos:
            return False
        if cur_column - i == abs(pos - queen_list[i]):
            return False
        i += 1
    return True

if __name__ == "__main__":
    eight_queens(4)
    print('\n--- solution count ---')
    print(solution_count)


"""
0-1背包
"""


"""
子集
"""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, tmp):
            ans.append(tmp)
            print(ans)
            for i in range(index, len(nums)):
                backtrack(i + 1, tmp + [nums[i]])

        ans = []
        backtrack(0, [])
        return ans

a = Solution()
a.subsets([1,2,3])

"""
子集2
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums: return []
        nums.sort()
        def backtrack(index,tmp):
            ans.append(tmp)
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1,tmp+[nums[i]])
        backtrack(0,[])
        return ans

"""
括号生成
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = ''
        def backtrack(cur,left,right):
            if left == 0 and right == 0:
                ans.append(cur)
                return
            if right < left:
                return
            if left > 0:
                backtrack(cur+'(',left-1,right)
            if right > 0:
                backtrack(cur+')',left,right-1)
        backtrack(cur,n,n)
        return ans

"""
组合总和
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtrack(i, target, tmp):
            if target == 0:
                ans.append(tmp[:])
                return
            if i == n or target < candidates[i]:
                return
            backtrack(i, target - candidates[i], tmp + [candidates[i]])
            backtrack(i + 1, target, tmp)

        backtrack(0, target, [])
        return ans

"""
电话号码字母组合
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}

        def backtrack(com,digit):
            if len(digit) == 0:
                ans.append(com)
            else:
                for letter in phone[digit[0]]:
                    backtrack(com+letter,digit[1:])
        ans = []
        backtrack('',digits)
        return ans

"""
单词搜索
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i, j, k, visited):
            if k == len(word):
                return True
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                tmp_x, tmp_y = i + dx, j + dy
                if 0 <= tmp_x < row and 0 <= tmp_y < col and (tmp_x, tmp_y) not in visited and board[tmp_x][tmp_y] == \
                        word[k]:
                    visited.add((tmp_x, tmp_y))
                    if dfs(tmp_x, tmp_y, k + 1, visited):
                        return True
                    visited.remove((tmp_x, tmp_y))
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, 1, {(i, j)}):
                    return True
        return False