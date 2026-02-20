from typing import List, Optional
import random
import heapq

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  #   INF = 10**9
    
  #   head = ListNode()
  #   tail = head
  #   currMin = INF
  #   while any(node for node in lists):
  #     currMin = INF
  #     for i, node in enumerate(lists):
  #       if node and node.val < currMin:
  #         currMin = node.val
  #         currBest = i
  #     bestNode = lists[currBest]
  #     lists[currBest] = bestNode.next
  #     bestNode.next = None
  #     tail.next = bestNode
  #     tail = tail.next
    
  #   return head.next
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
      if node:
        heapq.heappush(heap, (node.val, i, node))
    
    head = ListNode()
    tail = head
    
    while heap:
      _, i, node = heapq.heappop(heap)
      tail.next = node
      tail = tail.next
      if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))
      tail.next = None
    
    # curr = head.next
    # while curr:
    #   print(curr.val)
    #   curr = curr.next
    return head.next



def build_list(arr):
  dummy = ListNode()
  curr = dummy
  for v in arr:
    curr.next = ListNode(v)
    curr = curr.next
  return dummy.next

def print_list(head):
  arr = []
  while head:
    arr.append(head.val)
    head = head.next
  print(arr)

def generate_test_data(num_lists=5, max_len=6, value_range=(-10, 50)):
  lists = []
  for _ in range(num_lists):
    length = random.randint(0, max_len)
    arr = sorted(random.randint(*value_range) for _ in range(length))
    lists.append(build_list(arr))
  return lists

lists = generate_test_data()
sol = Solution()
sol.mergeKLists(lists)