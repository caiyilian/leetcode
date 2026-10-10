from typing import List

# @lc code=begin

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 二刷版：哈希集合 + 只从起点数（O(n)）
        if len(nums) == 0:               # ★ 空数组特判（漏了会 WA：max_length 初始 1 会返回 1）
            return 0
        hash_set = set(nums)             # 去重 + O(1) 查找
        max_length = 1
        for n in hash_set:               # 遍历集合（不是原数组）
            if n - 1 not in hash_set:    # ★ 核心：n-1 不在 = n 是序列起点，才从这里数
                len_each = 1
                while n + 1 in hash_set:  # 往后延伸
                    len_each += 1
                    n += 1
                max_length = max(max_length, len_each)
        return max_length


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))   # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(s.longestConsecutive([]))                        # 0
    print(s.longestConsecutive([1, 2, 0, 1]))              # 3