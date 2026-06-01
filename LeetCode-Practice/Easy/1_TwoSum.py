#题目：1.两数之和
#难度：Easy
#日期：2026.6.1
#思路：哈希字典，空间换时间
class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, val in enumerate(nums):
            need = target - val
            if need in dic:
                return [dic[need], index]
            dic[val] = index
