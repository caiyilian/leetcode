# Created by Chono-Hina at 2026/09/12 15:20
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(s)
        length_p = len(p)
        count_list = list(map(p.count, "abcdefghijklmnopqrstuvwxyz"))
        index_list = []
        last_match = False
        count_list_s = None
        for i in range(length - length_p + 1):
            if last_match:
                if s[i+length_p-1] == s[i-1]:
                    index_list.append(i)
                    last_match = True
                else:
                    last_match = False
                    count_list_s[ord(s[i-1])-97] -= 1
                    count_list_s[ord(s[i+length_p-1])-97] += 1
                continue
            if count_list_s is None:
                count_list_s = list(map(s[i: i+length_p].count, "abcdefghijklmnopqrstuvwxyz"))
            else:
                count_list_s[ord(s[i-1])-97] -= 1
                count_list_s[ord(s[i+length_p-1])-97] += 1
            if count_list_s == count_list:
                index_list.append(i)
                last_match = True
            else:
                last_match = False
        return index_list
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))
