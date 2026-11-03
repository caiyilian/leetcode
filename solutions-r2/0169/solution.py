"""169. 多数元素（二刷）——摩尔投票（用户 AC 版）

用户二刷（2026-11-03 22:46 提交 758483022，AC，15ms/21.5MB）
- 摩尔投票 Boyer-Moore：候选 now + 计数 count；相同 +1、不同 -1、归零换候选
- 正确性：多数元素出现 > n/2 次，抵消后必剩它（"投票抵消"思想）
- WA 复盘（22:45 758482865）：count==0 换候选时漏了 count=1 重置 → 需补上
- O(n)/O(1)，比排序/哈希更优（进阶首选）
"""

from typing import List


# ===== 用户 AC 版（摩尔投票） =====
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == now:
                count += 1
            else:
                count -= 1
                if count == 0:
                    now = nums[i]
                    count = 1        # ⚡ WA 复盘：换候选时必须重置计数！
        return now


# ===== 参考：同逻辑更紧凑写法 =====
class SolutionCompact:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if count == 0:           # 归零 → 换候选人
                now = n
            count += 1 if n == now else -1     # 相同 +1 / 不同 -1
        return now


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))                # 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))    # 2
    print(s.majorityElement([1]))                      # 1