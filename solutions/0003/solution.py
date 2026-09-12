# Created by Chono-Hina at 2026/09/12 14:31
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        max_length = 1
        start = 0
        now_length = 1
        index_dict = {s[0]: start}
        for i, c in enumerate(s[1:]):
            index_repeat = index_dict.get(c)
            if index_repeat is not None and index_repeat >= start:
                start = index_repeat + 1
                now_length = i + 2 - start
            else:
                now_length += 1
                max_length = max(now_length, max_length)
            index_dict[c] = i + 1
        return max(now_length, max_length)
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
