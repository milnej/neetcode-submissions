# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        curr = head
        nextNode = None
        if head.next:
            nextNode = head.next
        else:
            return head
    
        while nextNode:
            temp = nextNode.next
            nextNode.next = curr
            curr = nextNode
            nextNode = temp
        
        head.next = None
        
        return curr
