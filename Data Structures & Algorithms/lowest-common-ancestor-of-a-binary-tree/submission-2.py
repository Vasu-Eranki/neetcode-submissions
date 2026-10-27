# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            if not root or root==p or root==q:
                return root
            else:
                right_side = dfs(root.right,p,q) # try to find it on the right
                left_side = dfs(root.left,p,q) # try to find it on the left
                if(right_side and left_side):
                    return root 
                return right_side or left_side
        return dfs(root,p,q)
        