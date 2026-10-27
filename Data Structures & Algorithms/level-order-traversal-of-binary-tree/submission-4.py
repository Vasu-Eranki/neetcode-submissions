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
        queue = [root]
        results = []
        while(queue):
            results_for_this_level = []
            length = len(queue)
            for _ in range(length):
                root_of_interest = queue.pop(0)
                results_for_this_level.append(root_of_interest.val)
                if(root_of_interest.left):
                    queue.append(root_of_interest.left)
                if(root_of_interest.right):
                    queue.append(root_of_interest.right)
            results.append(results_for_this_level)
        return results
        