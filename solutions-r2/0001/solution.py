from typing import List

# @lc code=begin

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 二刷版：哈希表一次遍历（边查补数、边存当前值）
        hash_map = {}
        for i in range(len(nums)):
            if hash_map.get(target - nums[i]) is not None:
                return [i, hash_map[target - nums[i]]]
            hash_map[nums[i]] = i
        # 题目保证有唯一解，不会走到这里


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [1, 0]（或 [0, 1]）
    print(s.twoSum([3, 2, 4], 6))        # [2, 1]（或 [1, 2]）
    print(s.twoSum([3, 3], 6))           # [1, 0]（或 [0, 1]）