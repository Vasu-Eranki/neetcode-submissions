# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        value_to_idx = {inorder[idx]:idx for idx in range(len(inorder))}
        pre_idx = 0
        def recursive_solution(start:int,end:int)->Optional[TreeNode]:
            nonlocal pre_idx
            if (start>end):
                return None
            root_val = preorder[pre_idx]
            pre_idx+=1
            root = TreeNode(root_val)
            mid = value_to_idx[root_val]
            root.left = recursive_solution(start,mid-1)
            root.right = recursive_solution(mid+1,end)
            return root
        return recursive_solution(0,len(preorder)-1)

        