class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 二刷版：滑动窗口 + 字典记"字符 → 最后出现位置"（O(n) 最优解）
        # 用户 AC 版原样 + 标准优化注释
        length = len(s)
        if length == 0:
            return 0
        hash_map = {}                  # 字符 → 最后出现下标
        result = 0
        left = 0
        for right in range(length):
            if hash_map.get(s[right]) is not None:   # 当前字符在窗口内出现过 → 重复
                result = max(result, right - left)   # 先记当前窗口（不含 right）
                index = hash_map[s[right]]
                # 优化：标准写法不物理清空 dict，而是用 last[c] >= left 判断"过期"
                # 保留用户写法：逐个把窗口内到 index 的字符记录置 None
                for i in range(left, index):
                    hash_map[s[i]] = None
                left = index + 1                     # 左指针跳到重复位置 + 1
            hash_map[s[right]] = right               # 更新当前字符的最后位置
        result = max(result, right - left + 1)       # ★ 收尾：循环结束后最后一个窗口
        return result

        # ===== 标准更简版（不物理清空，靠 left 判过期）=====
        # last = {}
        # left = 0
        # best = 0
        # for right, c in enumerate(s):
        #     if c in last and last[c] >= left:      # 重复且仍在窗口内
        #         left = last[c] + 1
        #     last[c] = right
        #     best = max(best, right - left + 1)
        # return best