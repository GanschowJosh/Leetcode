# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        curr = head
        while curr != None:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next
        return None