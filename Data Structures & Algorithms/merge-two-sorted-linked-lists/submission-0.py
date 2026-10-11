# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2

        if p1 is None:
            return p2
        elif p2 is None:
            return p1

        result = None
        curr = None

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                nextNode = p1
                p1 = p1.next
            else:
                nextNode = p2
                p2 = p2.next
            
            if result is None:
                result = nextNode
                curr = nextNode
            else:
                curr.next = nextNode
                curr = curr.next
        
        if p1 is not None:
            curr.next = p1
        else:
            curr.next = p2

        return result
                