#题目：141.环形链表
#难度：Easy
#日期：2026.6.14
#思路：快慢指针，相遇则有环，不相遇则无环
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False