# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a placeholder for the result
        head = ListNode(0)
        
        # pointer for the result
        p = head
        
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            
        # append the remaining nodes of l1 or l2
        p.next = l1 if l1 else l2
        
        return head.next
