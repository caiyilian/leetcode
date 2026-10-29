"""22. 括号生成（二刷）——回溯：左右括号计数剪枝（O(C_n)/O(n) 标准解）

用户 AC 版（2026-10-29 16:44 提交 757624463，一次通过，0ms/19.2MB）
- 加左括号：已用左括号数 < n
- 加右括号：已用右括号数 < 已用左括号数（右永远不超左，保证合法）
- 用 num_left 和 len(path)-num_left（右括号数）两个量剪枝
- ⚡ 回溯三件套：append → 递归 → pop（与 17 字母组合同款骨架）
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        加右括号的条件是，之前左括号数量大于右括号数量
        加左括号的条件是，之前的左括号数量小于n
        """
        if n == 0:
            return []
        result = []

        def fun(path, num_left=0):
            if len(path) == 2 * n:
                result.append("".join(path))
                return path
            if len(path) - num_left < num_left:   # 右括号数 < 左括号数 → 可加右
                path.append(")")
                path = fun(path, num_left)
                path.pop()
            if num_left < n:                       # 左括号数 < n → 可加左
                path.append("(")
                path = fun(path, num_left + 1)
                path.pop()
            return path

        fun([])
        return result


# ===== 标准两变量版参考（left, right 分开传，更直观） =====
class SolutionClean:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, left, right):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if left < n:                            # 左括号还没用完
                path.append("(")
                dfs(path, left + 1, right)
                path.pop()
            if right < left:                        # 右括号不能超过左括号
                path.append(")")
                dfs(path, left, right + 1)
                path.pop()

        dfs([], 0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))   # 5 个
    print(s.generateParenthesis(1))   # ['()']
    print(s.generateParenthesis(0))   # []