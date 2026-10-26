# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveSolution(self,root:Optional[TreeNode],tracker:List[int]):
        if not root:
            return 
        self.recursiveSolution(root.left,tracker)
        tracker.append(root.val)
        self.recursiveSolution(root.right,tracker)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.recursiveSolution(root,results)
        return results
