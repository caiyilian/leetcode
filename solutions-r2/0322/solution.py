"""322. 零钱兑换（二刷）——完全背包一维 DP（用户 AC 版）

用户二刷（2026-11-02 14:05 提交 758173781，AC，431ms/19.5MB）
- RE 复盘（14:04 758173499）：内层直接 `dp[i-j]`，当硬币 j > 当前金额 i 时下标变负 → IndexError
- AC 修复：先 `coins.sort()`，内层遇到 `j > i` 直接 break（硬币有序 + 提前剪枝）
- 完全背包：每个硬币无限使用；dp[i] = 凑出金额 i 的最少硬币数
"""

from math import isinf
from typing import List


# ===== 用户 AC 版（排序 + break 剪枝） =====
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):        # 外层金额
            for j in coins:                # 内层硬币（完全背包可复用）
                if j > i:
                    break                  # ⚡ 排序后提前剪枝，也避免 dp[i-j] 负下标
                dp[i] = min(1 + dp[i - j], dp[i])
        return dp[amount] if isinf(dp[amount]) is False else -1


# ===== 参考：BFS 最短步数（把问题看成图） =====
from collections import deque


class SolutionBFS:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque([(amount, 0)])
        seen = {amount}
        while q:
            cur, steps = q.popleft()
            for c in coins:
                nxt = cur - c
                if nxt == 0:
                    return steps + 1
                if nxt > 0 and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))    # 3
    print(s.coinChange([2], 3))           # -1
    print(s.coinChange([1], 0))           # 0