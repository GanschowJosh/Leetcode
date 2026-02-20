# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1=[]
        stack=[root1]
        while stack:
            curr=stack.pop()
            if curr.left==None and curr.right==None: seq1.append(curr.val)
            if curr.left != None: stack.append(curr.left)
            if curr.right != None: stack.append(curr.right)
        seq2=[]
        stack=[root2]
        while stack:
            curr=stack.pop()
            if not curr.left and not curr.right: seq2.append(curr.val)
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
        return seq1==seq2