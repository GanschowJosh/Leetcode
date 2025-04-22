from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []
        def dfs(root, target, current_path):
            if not root:
                return
            current_path = current_path + [root.val]
            if (not root.left) and (not root.right): 
                if root.val == target:
                    out.append(current_path)
            dfs(root.left, target-root.val, current_path)
            dfs(root.right, target-root.val, current_path)
        dfs(root, targetSum, list())
        return out