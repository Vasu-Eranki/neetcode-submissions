# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(root:Optional[TreeNode])->int:
            boolean_flag = True
            if not root:
                return 0,boolean_flag
            left_height,left_flag = dfs(root.left)
            right_height,right_flag = dfs(root.right)
            if abs(right_height-left_height)>1:
                boolean_flag=False
            return 1+max(left_height,right_height), left_flag & right_flag & boolean_flag
        height, boolean_flag = dfs(root)
        return boolean_flag

        