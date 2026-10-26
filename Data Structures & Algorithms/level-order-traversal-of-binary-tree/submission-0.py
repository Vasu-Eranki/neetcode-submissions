# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        bfs = [root]
        while(bfs):
            length = len(bfs)
            results_for_this_level = []
            for i in range(len(bfs)):
                root_of_interest = bfs.pop(0)
                results_for_this_level.append(root_of_interest.val)
                if(root_of_interest.left):
                    bfs.append(root_of_interest.left)
                if(root_of_interest.right):
                    bfs.append(root_of_interest.right)
            results.append(results_for_this_level)
        return results
        
        