#题目：27.移除元素
#难度：Easy
#日期：2026.6.2
#思路：用慢指针指向放置保留元素的位置，用快指针遍历数组
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1;
        return k;