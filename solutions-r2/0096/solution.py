"""96. 不同的二叉搜索树（二刷）——DP 卡特兰数（O(n²)/O(n) 标准解）

用户 AC 版（2026-11-01 16:02 提交 758039077，一次通过，0ms/19.2MB）
- 解答注释里手推了 n=2/3 的案例，思路清晰：以 i 为根，左子树 j 个节点，右子树 i-1-j 个节点
- 递推：dp[i] = Σ_{j=0..i-1} dp[j] * dp[i-1-j]（左子树 j 个 × 右子树 i-1-j 个，枚举根节点位置）
- dp[0]=dp[1]=1；结果 = 卡特兰数 C(n)（闭式 C(2n,n)/(n+1)）
"""

from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                # 以 j 为左子树节点数，i-1-j 为右子树节点数（去掉根 i-1 个）
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))    # 5
    print(s.numTrees(1))    # 1
    print(s.numTrees(8))    # 1430