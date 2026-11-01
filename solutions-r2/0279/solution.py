"""279. 完全平方数（二刷）——DP 完全背包（O(n√n)/O(n) 标准解）

用户 AC 版（2026-11-01 19:49 提交 758075279，2538ms/19.1MB）—— DP 改版（内层 j²≤i）
- 递推：dp[i] = min(dp[i - j*j] + 1)，j 从 1 到 √i（枚举最后一个平方数）
- dp[0]=0，dp 初始 inf；答案 dp[n]
- ⚡⚡ 性能关键（一版 3938ms → 二版 2538ms 实证）：
  内层上界必须用 i（j² ≤ i）而非常数 n（j² ≤ n）——i 小时内层白扫大量 j
- 本题更优解：BFS（图最短步数）或数学法（四平方和定理答案只可能 1/2/3/4，<1ms）
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i + 1):          # ⚡ 上界用 i（j²≤i），不是 n
                if j ** 2 > i:
                    break
                dp[i] = min(dp[i - j ** 2] + 1, dp[i])
        return dp[n]


# ===== 数学法（拉格朗日四平方和定理，O(√n)，<1ms） =====
class SolutionMath:
    def numSquares(self, n: int) -> int:
        # 答案只可能是 1/2/3/4
        if int(n ** 0.5) ** 2 == n:                # ① 本身就是平方数 → 1 个
            return 1
        a = 1
        while a * a <= n:                          # ② 枚举 a，n-a² 也是平方数 → 2 个
            b = n - a * a
            if int(b ** 0.5) ** 2 == b:
                return 2
            a += 1
        while n % 4 == 0:                          # ③ 四平方和推论：n=4^k(8m+7) → 4 个
            n //= 4
        if n % 8 == 7:
            return 4
        return 3                                   # ④ 其余 → 3 个


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))    # 3
    print(s.numSquares(13))    # 2
    print(s.numSquares(4))     # 1