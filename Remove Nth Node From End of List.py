# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #window to hold the nth-1 from the end to the end 
        window = []
        current = head
        while current:
            if len(window) == n+1:
                window.pop(0)
            window.append(current)
            current = current.next
        
        #list only has one value or removing the head
        if len(window) == n:
            return head.next
        
        #otherwise, remove the nth node by skipping it 
        nth_prev = window[0] #node just before nth from the end (n-1th from the end)
        nth_prev.next = nth_prev.next.next if nth_prev.next else None

        return head

