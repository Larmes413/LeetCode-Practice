#题目：242. 有效的字母异位词
#难度：Easy
#日期：2026.6.5
#思路：用 26 个计数器：s 中出现的字母 +1，t 中出现的字母 -1，最后所有计数器必须为 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
