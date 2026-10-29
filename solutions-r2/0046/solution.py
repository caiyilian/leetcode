"""46. 全排列（二刷）——回溯 + used 标记（O(n×n!)/O(n) 标准解）

用户 AC 版（2026-10-29 17:21 提交 757634223，一次通过，0ms/19.6MB）
- 排列：顺序不同算不同 → 每层都要"回头"选所有没用过的数 → 用 exist(set) 标记已用
- ⚡ 与 39 组合总和对比：组合用 start 不回头（去重）；排列用 used 标记（允许回头）
- 递归三部曲：选（exist.add + path.append）→ 递归 → 撤销（path.pop + exist.remove）
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        length = len(nums)

        def fun(path, exist):
            if len(path) == length:
                result.append(path.copy())          # ★ copy：path 共享引用
                return path
            for n in nums:                          # ⚡ 每次都从全部数里选（回头）
                if n in exist:
                    continue                        # 已用过 → 跳过
                exist.add(n)                        # 选
                path.append(n)
                path = fun(path, exist)             # 递归
                path.pop()                          # 撤销
                exist.remove(n)
            return path

        fun([], set())
        return result


# ===== 标准 used 数组（下标）版参考 =====
class SolutionClean:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i, n in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(n)
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))   # 6 个
    print(s.permute([1]))         # [[1]]
    print(s.permute([]))          # []