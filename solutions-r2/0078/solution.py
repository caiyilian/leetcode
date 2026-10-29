"""78. 子集（二刷）——回溯 start 模板：每进节点收集当前路径（O(n×2^n)/O(n) 标准解）

用户 AC 版（2026-10-29 17:58 提交 757641849，一次通过，4ms/19.4MB）
- 子集 = 搜索树的所有节点（含空集）——每 append 一个元素即收集一次 path
- start 不回头（和 39 组合同款）：避免 [1,2] 和 [2,1] 重复
- result 初始 [[]]（空集）；另一等价写法是"选/不选"二分回溯（归档附参考）
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]                    # 空集
        length = len(nums)

        def fun(path, start):
            if len(path) == length:      # 满长度结束（其实不会超，边界保护）
                return path
            for i, n in enumerate(nums[start:]):
                path.append(n)
                result.append(path.copy())     # ★ 每进入一个节点就收集（子集=所有路径）
                path = fun(path, start + i + 1)  # 不回头
                path.pop()
            return path

        fun([], 0)
        return result


# ===== 标准"选/不选"版参考（更通用，可扩展到 90/491） =====
class SolutionClean:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])         # 选
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)             # 不选

        dfs(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))   # 8 个
    print(s.subsets([]))          # [[]]
    print(len(s.subsets([1, 2, 3, 4])))  # 16