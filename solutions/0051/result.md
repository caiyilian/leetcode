# 51. N 皇后 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 51. N 皇后（N-Queens）· **困难**（回溯家族收官题） |
| 链接 | https://leetcode.cn/problems/n-queens/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 9/9 用例通过** |
| 运行时间 | **7 ms（击败 90%）+ 内存击败 100%** |

## 解法（用户按提示独立完成：三集合 + 对角线编号 + 预生成行字符串）

```python
class Solution:
    def solveNQueens(self, n):
        result = []
        temp = ["."*j + "Q" + "."*(n-j-1) for j in range(n)]   # 预生成每列行字符串
        def fun(path, i, col, diag1, diag2):
            if i == n:                    # 放满 n 行（每行一个皇后 → 天然不同行）
                result.append(path.copy())
                return
            for j in range(n):
                if j not in col and (i+j) not in diag1 and (i-j) not in diag2:
                    path.append(temp[j])
                    col.add(j)
                    diag1.add(i+j)        # ↘ 对角线编号（同一斜线 i+j 相等）
                    diag2.add(i-j)        # ↙ 对角线编号（同一斜线 i-j 相等）
                    fun(path, i+1, col, diag1, diag2)
                    path.pop()
                    col.remove(j)         # 回溯撤销三集合
                    diag1.remove(i+j)
                    diag2.remove(i-j)
        fun([], 0, set(), set(), set())
        return result
```

**用户的直觉（提示前就有）**："每行一个皇后 + 列限制 + 对角线限制，回溯时去掉"——方向全对；提示只是把"对角线放位置列表"升级为"放对角线编号集合"（i+j / i-j 恒等号即编号）。

## 验证

- **n=1..9 方案数完美命中标准序列**：1, 0, 0, 2, 10, 4, 40, 92, 352；
- 与独立"位标记布尔数组"实现逐项一致；
- 官方样例 n=4 两种摆法正确、n=1 单皇后正确。

## 复杂度

- 时间 **O(n!)**（首行 n 选、随后逐层剪枝，最坏 n! 量级；n ≤ 9 秒级）；空间 **O(n)**（三集合 + 递归栈）。

## 🌳 回溯家族 8/8 全通关！