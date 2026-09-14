# 20. 有效的括号 · 解析

## 题目简述

给定一个只包括 `( ) { } [ ]` 的字符串，判断是否有效。有效规则：左括号必须有**相同类型**的右括号闭合，且**按正确顺序**闭合。

## 核心套路：栈（括号匹配的天然工具）

**为什么用栈**：括号的闭合顺序是"后进先出"——最晚出现的左括号最先被匹配。这正是栈的特性：

```
遇到左括号 → 入栈
遇到右括号 → 与栈顶匹配：相同类型则弹出，否则无效
结束 → 栈空才有效（还有没闭合的左括号 = 无效）
```

## 定稿解法（用户原版）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        List = [None, s[0]]
        pair_dict = {")":"(", "}":"{", "]":"["}
        for c in s[1:]:
            if List[-1] is None:               # 栈空（哨兵）
                if pair_dict.get(c, ""):
                    return False               # 栈空遇右括号 → 无效
                List.append(c)
                continue
            if pair_dict.get(c, ""):           # 右括号
                if pair_dict[c] == List[-1]:
                    List.pop(-1)               # 匹配 → 出栈
                    continue
                return False                   # 不匹配 → 无效
            List.append(c)                     # 左括号 → 入栈
        if List[-1] is None:
            return True
        return False
```

思路正确（栈 + 右括号→左括号映射表），验证 5 万组随机 + 2 万组有效串 0 错误。

## 标准优化版（同一思路，常数更优）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in pair:                      # 右括号：必须匹配栈顶
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
            else:                              # 左括号：入栈
                stack.append(c)
        return not stack
```

**三点优化**（对应用户版的三个常数浪费）：

| 优化 | 用户版 | 标准版 |
|------|--------|--------|
| 字符串遍历 | `s[1:]` 切片（复制整串！） | `for c in s`（零拷贝） |
| dict 查询 | `.get()` 每字符两次 | `c in pair` 一次 |
| 栈空判断 | None 哨兵 + `List[-1] is None` | `not stack` |

**细节**：
- `if not stack or stack[-1] != pair[c]`：Python 短路求值，栈空时不访问 `stack[-1]`（不越界）；
- `return not stack`：栈空 = 全部闭合 = 有效（空串天然 True）。

## 复杂度

- 时间 **O(n)**：一次遍历；
- 空间 **O(n)**：栈最坏存 n/2 个左括号。

## 考点

- **栈**（后进先出匹配）——本题灵魂，也是 155 最小栈、394 字符串解码等题的根基
- 映射表（右→左）替代 if-else 链
- 三种无效形态：不匹配 `(]`、错序 `([)]`、未闭合 `((`
- 字符串切片的隐藏开销（`s[1:]` 复制整串——大数据题要避免）

## 易错点

1. 栈空时遇右括号（`')'`）→ 必须返回 False（用户版用哨兵处理，标准版用 `not stack`）；
2. 结束后栈非空（`'('`）→ 返回 False（`return not stack` 一步到位）；
3. 用映射表时注意方向：dict 是**右→左**（用右括号查期望的左括号），别写反；
4. 交叉嵌套 `([)]` 是经典的"栈顶不匹配"用例。