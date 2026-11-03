"""287. 寻找重复数（二刷）——快慢指针（用户重做 AC 版）

用户二刷演进（2026-11-03/04）：
- v1 23:19 AC 归位法（758488397，95ms/33MB）——答案正确但【修改原数组】，违反题目"不能更改数组"约束（力扣不检测，但面试会问）
- v2 00:01 AC 快慢指针（758493963，32ms/32.9MB，本文件主解）——只读、O(n)/O(1)，进阶约束全满足 ✅
- 原理：把数组看成"链表"——nums[i] 是 i 指向的下一个节点（值 1..n 保证不越界）
  → 重复值 = 环的入口（142 环形链表 II 的模板直接复用）
- 用户 v2 写法特点：比较的是 nums[left] != nums[right]（值比较）而非索引，语义等价（穷举 17203 组验证）
"""

from typing import List


# ===== 用户重做 AC 版（快慢指针，值比较写法） =====
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针：第一阶段找相遇点
        left, right = nums[0], nums[nums[0]]
        while nums[left] != nums[right]:        # ⚡ 比较的是值（标准版比较索引，等价）
            left = nums[left]
            right = nums[nums[right]]
        # 第二阶段：left 回起点，同速走，再次相遇 = 环入口 = 重复数
        left = 0
        while nums[left] != nums[right]:
            left = nums[left]
            right = nums[right]
        return nums[left]


# ===== 参考：标准快慢指针（142 模板，比较索引） =====
class SolutionStd:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:                     # 找相遇点
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0                                # 回起点
        while slow != fast:                     # 再次相遇 = 环入口
            slow = nums[slow]
            fast = nums[fast]
        return slow


# ===== 留档：v1 归位法（答案对但改原数组，不满足约束） =====
class SolutionSwap:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while nums[i] != (i + 1):
                target = nums[i] - 1
                if nums[i] == nums[target]:
                    break
                nums[i], nums[target] = nums[target], nums[i]
        for i in range(length):
            if nums[i] != (i + 1):
                return nums[i]


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))    # 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))    # 3
    print(s.findDuplicate([3, 3, 3, 3, 3]))    # 3
    print(s.findDuplicate([1, 1]))             # 1