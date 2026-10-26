# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_idx = inorder_idx = 0 
        def dfs(limit):
            nonlocal preorder_idx,inorder_idx
            if preorder_idx >=len(preorder):
                return None 
            if inorder[inorder_idx]==limit:
                inorder_idx+=1
                return None 
            root = TreeNode(preorder[preorder_idx])
            preorder_idx+=1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))
