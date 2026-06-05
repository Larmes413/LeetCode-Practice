#题目：283. 移动零
#难度：Easy
#日期：2026.6.3
#思路：把所有非零元素按顺序移到数组前面，然后在末尾补零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroIndex] = nums[i]
                nonZeroIndex += 1
        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
