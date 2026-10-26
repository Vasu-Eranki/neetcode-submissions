# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k 
        result = root.val
        def inorder(root):
            if not root:
                return
            nonlocal count,result
            inorder(root.left)
            count-=1
            if(count==0):
                result = root.val
            inorder(root.right)
        inorder(root)
        return result
        