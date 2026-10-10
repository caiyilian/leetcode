from typing import List
from collections import defaultdict

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 二刷版：计数法 key（一刷定稿解法的直接复用）
        # 字母异位词本质 = 各字母出现次数相同 → 用 26 长度计数数组的 tuple 当 key
        hash_map = defaultdict(list)
        for word in strs:
            cnt = [0] * 26                 # 统计当前单词的字母频次
            for c in word:
                cnt[ord(c) - 97] += 1      # 'a' 的 ord 是 97
            hash_map[tuple(cnt)].append(word)   # tuple 可哈希，才能当 dict key
        return list(hash_map.values())


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]（组间/组内顺序任意）