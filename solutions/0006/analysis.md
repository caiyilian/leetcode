# 6. Z 字形变换 · 解题解析

## 一句话思路

不真正去画二维网格，只模拟**字符在行之间的游走**：行号从 0 走到 `numRows-1`，触底折返回到 0，循环往复——走到哪行，字符就进哪行。

## 核心洞察

字符的落点只由**当时的行号**决定，与列无关。因此维护 `numRows` 个桶（每行一个字符串），游走时把当前字符丢进对应桶，最后按行拼接即得答案。

## 方法一：按行模拟（推荐，直观不易错）

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s                      # 特判：一行时不会"折返"，直接返回
        rows = [""] * numRows
        row, direction = 0, 1
        for ch in s:
            rows[row] += ch
            row += direction
            if row == 0 or row == numRows - 1:   # 触顶 / 触底 → 换方向
                direction = -direction
        return "".join(rows)
```

- **时间复杂度**：O(n)，每个字符处理一次
- **空间复杂度**：O(n)，存储结果
- **易错点**：
  1. `numRows == 1` 忘了特判会死循环（direction 永远翻转、row 在 0/1 间横跳）
  2. 换方向要在「移动之后」判断，否则边界行会漏字符

## 方法二：周期公式（面试进阶加分）

一个完整的「下 → 上」周期长度为 `t = 2 * numRows - 2`。按行直接"跳着取"：

- **第 0 行 / 最后一行**：每个周期取 1 个字符 —— `i = k·t`、`i = k·t + numRows - 1`
- **中间行 r**（1 ≤ r ≤ numRows-2）：每个周期取 2 个 —— `i = k·t + r` 与 `i = (k+1)·t - r`

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        t = 2 * numRows - 2
        ans = []
        for r in range(numRows):
            k = 0
            while k * t + r < len(s):
                ans.append(s[k * t + r])                 # 每周期第一个
                if 0 < r < numRows - 1:
                    j = (k + 1) * t - r                  # 中间行的第二个
                    if j < len(s):
                        ans.append(s[j])
                k += 1
        return "".join(ans)
```

- 时间复杂度 O(n)，空间 O(n)（省掉了行桶数组，直接用下标取）

## 本题考点

| 考点 | 内容 |
|------|------|
| 模拟 | Z 字形游走的方向翻转 |
| 数学归纳 | 找到周期 `t = 2*numRows-2` 的下标规律 |
| 边界处理 | numRows=1、字符串结尾截断 |

## 提交记录

- 本地测试：3/3 通过
- 服务器提交：**1158/1158 通过**（隐藏用例全部通过）
- 性能：Runtime 7 ms（击败 89%）、Memory 19.2 MB