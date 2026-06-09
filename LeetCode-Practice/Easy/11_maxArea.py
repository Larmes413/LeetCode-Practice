#题目：11.盛最多水的容器
#难度：Easy
#日期：2026.6.9
#思路：用两个指针从两端向中间移动，每次计算当前水量，然后移动较短的线
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water