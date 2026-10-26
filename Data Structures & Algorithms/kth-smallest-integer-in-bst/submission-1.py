# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth_smallest = []
        def inorder(root,count:list[int]):
            if not root:
                return 
            inorder(root.left,count)
            count[0]-=1
            if(count[0]==0):
                kth_smallest.append(root.val)
            inorder(root.right,count)
        inorder(root,[k])
        return kth_smallest[0]