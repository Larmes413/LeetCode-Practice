#题目：1344.反转字符串
#难度：Easy
#日期：2026.6.10
#思路：双指针原地反转
    class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1