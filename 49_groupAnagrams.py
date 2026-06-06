#题目：49. 字母异位词分组
#难度：Easy
#日期：2026.6.6
#思路：字母异位词经过重新排序后会得到相同的字符串
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)
        return list(anagram_map.values())