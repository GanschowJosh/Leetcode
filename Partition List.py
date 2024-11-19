# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        less_end = less     #holds pointer to last element of less list for appending
        greater = ListNode(0)
        greater_end = greater

        while head != None:
            if head.val >= x: #greater than x
                greater_end.next = head
                greater_end = greater_end.next
            else: #less than x
                less_end.next = head
                less_end = less_end.next
            
            head = head.next
        
        greater_end.next = None #terminates list to avoid a cycle

        less_end.next = greater.next #conjoins lists

        return less.next #final list
