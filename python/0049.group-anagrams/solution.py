# Created by Chono-Hina at 2026/09/11 12:53
# leetgo: 1.4.18
# https://leetcode.cn/problems/group-anagrams/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_dict = {}
        for each_str in strs:
            sorted_str = "".join(sorted(list(each_str)))
            if sorted_str_dict.get(sorted_str) is None:
                sorted_str_dict[sorted_str] = [each_str]
            else:
                sorted_str_dict[sorted_str].append(each_str)
        return list(sorted_str_dict.values())

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
