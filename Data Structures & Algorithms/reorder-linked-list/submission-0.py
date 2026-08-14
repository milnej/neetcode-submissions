# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def recur(head, curr):
            if not curr:
                return head
            
            head = recur(head, curr.next)
            if not head:
                return None
            
            temp = None
            if head == curr or head.next == curr:
                curr.next = None
            else:
                temp = head.next
                head.next = curr
                curr.next = temp

            return temp


        
        recur(head, head)

      