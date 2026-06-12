#题目：125.验证回文串
#难度：Easy
#日期：2026.6.11
#思路：双指针从字符串两端往中间移动，比较字符是否相同
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True