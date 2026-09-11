# Created by Chono-Hina at 2026/09/11 12:53
# leetgo: 1.4.18
# https://leetcode.cn/problems/group-anagrams/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_dict = defaultdict(list)
        for each_str in strs:
            cnt = [0] * 26
            for s in each_str:
                cnt[ord(s) - 97] += 1
            sorted_str_dict[tuple(cnt)].append(each_str)
        return list(sorted_str_dict.values())

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
