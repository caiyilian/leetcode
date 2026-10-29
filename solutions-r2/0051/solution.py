"""51. N 皇后（二刷）——回溯 + 三集合查冲突（O(n!)/O(n) 标准解）

用户 AC 版（2026-10-29 17:42 提交 757638858，一次通过，11ms/19.6MB）
- 按行放皇后（每行必须恰好一个 Q）
- 冲突判定用三个集合：列 j、主对角线 i-j、副对角线 i+j（⚡ 对角线用行列差/和定标）
- 回溯三件套：ban.add + path.append → 递归 → ban.remove + path.pop
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        按行摆放
        首先，不在同一列就是j不相同
        不在对角线
        斜率为正的对角线：i j, i-1,j+1 所以就是 i+j 不变
        斜率为负的对角线：i j, i-j 不变
        """
        ban_j = set()      # 已占用的列
        ban_ipj = set()    # 已占用的副对角线（i+j 恒定）
        ban_idj = set()    # 已占用的主对角线（i-j 恒定）
        result = []

        def fun(path, i=0):
            if len(path) == n:
                result.append(path.copy())          # ★ copy
                return
            for j in range(n):
                if (j in ban_j) or (i - j in ban_idj) or (i + j in ban_ipj):
                    continue                        # 列/主对/副对 任一冲突 → 跳过
                ban_j.add(j)
                ban_ipj.add(i + j)
                ban_idj.add(i - j)
                path.append("." * j + "Q" + "." * (n - j - 1))   # 生成该行字符串
                fun(path, i + 1)
                ban_j.remove(j)
                ban_ipj.remove(i + j)
                ban_idj.remove(i - j)
                path.pop()

        fun([])
        return result


if __name__ == "__main__":
    s = Solution()
    for n in (1, 2, 4, 8):
        print(f"n={n}: {len(s.solveNQueens(n))} 个解")
    print(s.solveNQueens(4))