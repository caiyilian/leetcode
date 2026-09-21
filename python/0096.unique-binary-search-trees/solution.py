# Created by Chono-Hina at 2026/09/21 16:58
# leetgo: 1.4.18
# https://leetcode.cn/problems/unique-binary-search-trees/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numTrees(self, n: int) -> int:
        # 卡特兰数 DP：dp[i] = i 个节点的 BST 数量
        # 以 j 为根，左子树 j 个节点、右子树 i-1-j 个节点
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numTrees(n)
    print("\noutput:", serialize(ans, "integer"))
