"""70. 爬楼梯（二刷）——DP：斐波那契（O(n)/O(1) 滚动数组最优）

用户 AC 版（2026-11-01 15:39 提交 758034355，最终版滚动数组，0ms/19MB）
- 今天 4 次提交全部 AC，是一条漂亮的渐进优化链：
  v1 带记忆递归（758033078）→ v2 一维 DP 数组（758033666）→ v3 滚动数组（758034230/355）
- 递推：dp[i] = dp[i-1] + dp[i-2]（到第 i 阶 = 从 i-1 迈 1 步 + 从 i-2 迈 2 步）
- dp[0]=1, dp[1]=1（起点和第一级都是 1 种方式）
- 滚动数组：只保留前两个状态，空间 O(1)（本质就是斐波那契数列）
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 滚动数组（最终版，O(1) 空间）
        dp_ip1 = 1   # dp[1]
        dp_ip2 = 1   # dp[0]
        for _ in range(2, n + 1):
            dp_ip1, dp_ip2 = dp_ip1 + dp_ip2, dp_ip1
        return dp_ip1


# ===== 参考：一维 DP 数组（v2，O(n) 空间，思路最直白） =====
class SolutionDP:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# ===== 参考：带记忆的递归（v1，自顶向下） =====
class SolutionMem:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def fun(n):
            if n == 1 or n == 0:
                return 1
            if n not in mem:
                mem[n] = fun(n - 1) + fun(n - 2)
            return mem[n]

        return fun(n)


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))    # 2
    print(s.climbStairs(3))    # 3
    print(s.climbStairs(45))   # 1836311903