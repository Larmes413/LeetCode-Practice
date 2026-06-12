#题目：206.反转链表
#难度：Easy
#日期：2026.6.12
#思路：用三个指针（prev、curr、next_temp）遍历链表，逐个将当前节点的next指向前一个节点，最后返回prev作为新头节点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev