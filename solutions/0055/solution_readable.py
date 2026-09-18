# -*- coding: utf-8 -*-
"""
第 55 题 跳跃游戏 · 标准贪心版（维护"最远可达位置" far）

与用户版（solution.py，last_max/last_index 两变量绕版）10 万组对拍 0 差异。

核心：贪心只维护一个状态 far = 到目前为止最远能到哪，一次扫描：
  - i > far → 当前位置都到不了（有坑）→ False
  - far = max(far, i + nums[i]) → 更新最远可达

与 121 同一骨架（贪心 = 维护全局最优状态 + 一次扫描）：
  121: min_price = min(min_price, p)
  55 : far = max(far, i + nums[i])
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0                              # 最远能到哪
        for i, n in enumerate(nums):
            if i > far:                      # 当前位置到不了 → 有坑
                return False
            far = max(far, i + n)            # 更新最远可达
        return True