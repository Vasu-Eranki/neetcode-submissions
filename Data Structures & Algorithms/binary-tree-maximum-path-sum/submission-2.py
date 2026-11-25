# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxValue = -float('inf')
        def dfs(root):
            nonlocal maxValue 
            if not root:
                return 0
            left_sum = max(dfs(root.left),0)
            right_sum = max(dfs(root.right),0)
            maxValue = max(maxValue,left_sum+right_sum+root.val)
            return root.val+max(left_sum,right_sum,0)
        result = dfs(root)
        return maxValue

        
        