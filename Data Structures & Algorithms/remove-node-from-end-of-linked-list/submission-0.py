# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n == 0:
            return head
        
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        
        if n == length:
            return head.next
        
        curr = head
        prev = None
        index = 0
        while curr is not None:
            if index == length - n:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            index += 1
        
        return head
