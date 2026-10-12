from typing import List

# @lc code=begin

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 二刷版：定长滑动窗口 + 26 计数数组（标准最优解 O(n)/O(1)）
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:               # ★ s 比 p 短 → 不可能有异位词（漏了会 RE：初始化越界）
            return []
        counts = [0] * 26               # p 的字符计数
        now = [0] * 26                  # 当前窗口的字符计数
        for i in range(len_p):          # 初始化第一个窗口 [0, len_p-1]
            counts[ord(p[i]) - 97] += 1
            now[ord(s[i]) - 97] += 1
        results = []
        if counts == now:               # 第一个窗口就是异位词
            results.append(0)
        for i in range(len_p, len_s):   # 滑动：右进一个 +1、左出一个 -1
            now[ord(s[i]) - 97] += 1
            now[ord(s[i - len_p]) - 97] -= 1
            if counts == now:           # 计数相同 = 异位词，记录窗口起点
                results.append(i - len_p + 1)
        return results


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))   # [0, 6]
    print(s.findAnagrams("abab", "ab"))          # [0, 1, 2]
    print(s.findAnagrams("aaaaaaaaaa", "aa"))    # [0..8]
    print(s.findAnagrams("a", "ab"))             # []