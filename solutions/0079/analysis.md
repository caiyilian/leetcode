# 79. 单词搜索 · 解析

## 题目简述

`m×n` 网格中找单词（字母可上下左右相邻，**同一格不能重复用**）。存在返回 True。

## 核心套路：网格 DFS + 原地标记 + 回溯撤销（200 岛屿的"回溯版"）

**和 200 岛屿数量的关系**：

| | 200 岛屿数量 | 79 单词搜索 |
|--|------------|------------|
| 遍历 | DFS 泛洪（沉没整片） | DFS 按 word 逐字符匹配 |
| 标记 | 原地 '1'→'0'（**不撤销**） | 原地改 ''（**必须撤销**！） |
| 撤销 | 不需要（数完就完） | **需要**（换路径再试时格子要复原） |

**唯一区别：79 要"撤销"**——因为同一次搜索要尝试多条路径，走过的格子必须还原，否则别的路径没法复用。**这就是回溯"擦脚印"在网格上的应用。**

## 定稿（用户修复版）

```python
class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        length = len(word)
        def fun(i, j, index):
            if index == length:                    # ① 匹配完整个单词 → 成功（放最前！）
                return True
            if i < 0 or j < 0 or i >= m or j >= n: # ② 越界 → 走不通
                return False
            if board[i][j] != word[index]:         # ③ 字符不符 → 失败
                return False
            ori = board[i][j]
            board[i][j] = ""                       # ④ 标记访问（防回头）
            if fun(i+1, j, index+1):
                return True
            if fun(i-1, j, index+1):
                return True
            if fun(i, j+1, index+1):
                return True
            if fun(i, j-1, index+1):
                return True
            board[i][j] = ori                      # ⑤ 撤销（回溯）
            return False                           # ⑥ 全失败 → False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if fun(i, j, 0):
                        return True
        return False
```

## ⚠️ 本次实战教训：基线声明 vs 副作用依赖（IndexError 根源）

**用户原版的写法**（错误）：

```python
if 越界:
    return index == length    # 把"越界且匹配完"当成功条件
```

**为什么错**：成功（匹配完整单词）应该是**独立的基线**，不应该寄在"越界"这个巧合上。匹配完最后一个字符后（index == length），下一步：
- 恰好走出棋盘 → 原版逻辑碰巧成立（2x2 找 abcd 就是这种侥幸）；
- 还在棋盘内 → 执行 `board[i][j] != word[index]` → `word[length]` **越界崩溃**（3x3 找 "a" 就是力扣的用例）。

**正确顺序**（本版）：

```
① index == length → True（匹配完成，立即成功，不再查格子）
② 越界 → False（空间走完）
③ 字符不符 → False
```

**记忆锚点：递归基线按"目标的进度"声明（index==length），不要按"环境的副作用"（越界）声明。** 同理"空输入"等边界也要显式处理，不能指望碰巧。

## 复杂度

- 时间 **O(m·n·3^L)**（L = 词长；每格最多 4 方向，来路已标记所以实际 3 分支，指数于词长）；
- 空间 **O(L)** 递归栈（原地标记，无额外 visited 数组）。

## 考点

- 网格 DFS（200 岛屿的兄弟题）
- **回溯撤销**（换路径复用格子）
- 递归基线的正确声明（本此修复的核心）
- 原地标记 vs visited 数组

## 易错点

1. **基线顺序**：`index == length` 必须放最前（否则 word[index] 越界）；
2. **忘撤销**：`board[i][j] = ori` 漏了 → 路径间互相污染，False 误判；
3. 主循环只从 `word[0]` 匹配的格子开始（小剪枝，不写也行但白跑）；
4. 同格不能重复用（标记 '' 就是防这个）；
5. 对角不算相邻（只 4 方向）。

## 关联题

- **200 岛屿数量**（网格 DFS，不撤销）；
- **212 单词搜索 II**（多词版：Trie + DFS 剪枝，208 + 79 的组合）；
- 回溯家族收官在即（剩 131 分割回文串 / 51 N皇后）。