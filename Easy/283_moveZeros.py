class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroIndex] = nums[i]
                nonZeroIndex += 1
        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
