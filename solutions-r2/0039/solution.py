"""39. 组合总和（二刷）——回溯：可重复选 + 不回头（O(指数)/O(target) 标准解）

用户 AC 版（2026-10-29 17:08 提交 757630851，一次通过，8ms/19.6MB）
- ⚡ 妙点：同一个 start 变量管两件事——递归传 start（允许重复选当前数）+ 循环内 start+=1（不回头，去顺序重复）
- 先排序 → 循环里 now_sum+n > target 直接 break（后续更大，安全剪枝）
- 回溯三件套（append→递归→pop）+ path.copy() 收集（防引用共享）
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def fun(path, now_sum=0, start=0):
            if now_sum == target:
                result.append(path.copy())          # ★ copy：path 后续还会被修改
                return path
            if now_sum > target:
                return path
            for n in candidates[start:]:            # 从 start 开始（不回头）
                if now_sum + n > target:
                    break                            # 已排序：后面更大，剪枝
                path.append(n)
                path = fun(path, now_sum + n, start)  # 传 start：可重复选当前数
                path.pop()
                start += 1                            # 本层循环自增：下一个数才可选
            return path

        fun([])
        return result


# ===== 标准索引版参考（dfs(i) 选/不选 更直观） =====
class SolutionClean:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or cur > target:
                return
            path.append(candidates[i])                # 选当前（可重复）
            dfs(i, path, cur + candidates[i])
            path.pop()
            dfs(i + 1, path, cur)                     # 不选当前，向后

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))   # [[2,2,3],[7]]
    print(s.combinationSum([2, 3, 5], 8))      # [[2,2,2,2],[2,3,3],[3,5]]
    print(s.combinationSum([2], 1))            # []
    print(s.combinationSum([], 5))             # []