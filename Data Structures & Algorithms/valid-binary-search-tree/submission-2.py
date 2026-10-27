# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_limit,max_limit):
            if not node:
                return True
            if node.val>min_limit and node.val<max_limit:
                # check recursively underneath 
                right_side = dfs(node.right,node.val,max_limit)
                left_side = dfs(node.left,min_limit,node.val)
                return right_side and left_side
            else:
                return False
        return dfs(root,-math.inf,math.inf)

        