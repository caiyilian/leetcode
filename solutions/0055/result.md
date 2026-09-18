# 55. 跳跃游戏 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 55. 跳跃游戏（Jump Game）· 中等（贪心分类第 2 题） |
| 链接 | https://leetcode.cn/problems/jump-game/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 178/178 用例通过**（leetgo 复提交） |
| 运行时间 | 27 ms（leetgo 噪声，击败 35%） |
| 内存 | 20 MB |

## 解法（用户版 + 标准贪心版）

**用户版**（last_max/last_index 两变量绕版，逻辑碰巧完备）：

```python
def canJump(self, nums):
    if len(nums) == 1: return True
    if nums[0] == 0: return False
    nums.pop()
    last_max, last_index = float("-inf"), -1
    for i, num in enumerate(nums):
        if num == 0 and last_max - i + last_index == 0: return False
        if (num >= last_max) or (num + (i - last_index) > last_max):
            last_max = num; last_index = i
    return True
```

**标准贪心版**（solution_readable.py，far 单变量 4 行）：

```python
def canJump(self, nums):
    far = 0
    for i, n in enumerate(nums):
        if i > far: return False          # 有坑跳不过去
        far = max(far, i + n)             # 更新最远可达
    return True
```

## 核心理解（用户疑问解答）

- **是否符合要求**：O(n) 一次遍历 + O(1) 空间，满足 ✅；
- **是否 DP**：不是 DP，是**贪心**——但和 121 同一骨架（"维护全局最优状态 + 一次扫描"）：
  - 121 维护 `min_price`（历史最低价）
  - 55 维护 `far`（最远可达）
- **用户版绕在哪**：把"最远可达位置"这个单一概念拆成 `last_max`（值）+ `last_index`（下标）两个变量，再拼回 `last_max - i + last_index == 0` 的魔法判断——标准版一个 `far` 变量就表达清楚了。

## 验证

- 对拍 **10 万组随机数组 vs 标准贪心 0 不一致**；
- 官方样例：`[2,3,1,1,4]→true`、`[3,2,1,0,4]→false`；
- 边界：`[0]→true`、`[2,0,0]→true`、`[1,0,1,0]→false`。

## 复杂度

- 时间 **O(n)**；空间 **O(1)**。