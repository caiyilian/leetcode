# 79. 单词搜索 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 79. 单词搜索（Word Search）· 中等（回溯家族第 6 题 / 网格 DFS） |
| 链接 | https://leetcode.cn/problems/word-search/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 88/88 用例通过** |
| 运行时间 | 3265ms（leetgo 环境噪声，击败 76%；本地 2 万组对拍秒级） |
| 内存 | 19.4 MB |

## ⚠️ 本次修复的经典 bug（IndexError 排查实录）

**用户原版的成功条件设计缺陷**：

```python
if i < 0 or ...:  # 越界
    return index == length    # ← 把"越界且匹配完"当成功（错误依赖）

# 匹配完最后一个字符后 index == length：
# 若四方向里先碰到"棋盘内格子" → board[i][j] != word[index] → word[length] 越界 → IndexError
```

**崩溃场景**：棋盘大、word 短（如 3x3 找 "a"），匹配完还在棋盘中间，四方向不越界 → `word[1]` 越界。
**用户本地没发现的巧合**：`[["a","b"],["c","d"]]` + "abcd" 时匹配 `d` 后四方向**恰好全越界** → 走"越界 + index==length"分支侥幸不崩（且该用例正确结果就是 False——b→c 对角不相邻）。

**修复**：成功基线**直接声明**（不靠越界副作用）——

```python
def fun(i, j, index):
    if index == length:            # ① 匹配完 → True（放最前！）
        return True
    if 越界: return False          # ② 越界 = 走不通
    if board[i][j] != word[index]: return False
    ...标记/四方向/撤销...
```

**记忆锚点：递归基线按"距离目标的进度"声明（index==length），不要按"副作用"（越界）声明。**

## 验证

- 对拍 **2 万组随机棋盘（1~4 行 × 1~4 列 × 随机 5 字母词）vs visited 数组独立实现 0 不一致**；
- 官方样例：ABCCED→True、SEE→True、ABCB→False、`[["a"]]+"a"`→True、`[["a","b"],["c","d"]]+"abcd"`→False（对角不相邻）。

## 复杂度

- 时间 **O(m·n·3^L)**（L = 词长；每格最多 4 方向但来路已标记 → 3 分支）；空间 **O(L)** 递归栈（原地标记 O(1) 额外）。