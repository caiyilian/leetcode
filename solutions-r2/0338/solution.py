"""338. 比特位计数（二刷）——位运算 DP（用户 AC 版）⚡ 考前复习公式

用户二刷（2026-11-04 10:49 提交 758522891，AC 一次通过，3ms/20MB）
- 核心公式（考前看一眼）：dp[i] = dp[i>>1] + (i&1)
  理由：i 的二进制 = (i>>1) 的二进制 再补上最低位 → 1 的个数 = 去掉最低位后的个数 + 最低位
- ⚡ 括号坑（用户亲自踩的）：(i&1) 的括号不能去！Python 优先级 + > &，
  `dp[i>>1] + i & 1` 会被解析成 `(dp[i>>1] + i) & 1` → 结果全错
- 记忆锚点：位运算（&|^<<>>）优先级都低于加减乘除——混用必加括号
"""

from typing import List


# ===== 用户 AC 版（位运算 DP，O(n)） =====
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)      # ⚡ (i&1) 括号必须加！
        return dp


# ===== 参考：内置 bit_count（一行解，非面试写法但可亮） =====
class SolutionBuiltin:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))     # [0,1,1]
    print(s.countBits(5))     # [0,1,1,2,1,2]
    print(s.countBits(0))     # [0]