#题目：21.合并两个有序链表
#难度：Easy
#日期：2026.6.13
#思路：双指针比较，谁小谁接入结果链表
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        dummy = ListNode()
        r = dummy
        while p and q:
            if p.val >= q.val:
                r.next = q
                q = q.next
            else:
                r.next = p
                p = p.next
            r = r.next
        while p:
            r.next = p
            p = p.next
            r = r.next
        while q:
            r.next = q
            q = q.next
            r = r.next
        return dummy.next