# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        results = []
        while(queue):
            length = len(queue)
            results_for_this_level = []
            for idx in range(0,length):
                root_of_interest = queue.pop(0)
                if(root_of_interest.left):
                    queue.append(root_of_interest.left)
                if(root_of_interest.right):
                    queue.append(root_of_interest.right)
                if(idx==length-1):
                    results_for_this_level.append(root_of_interest.val)
            results.extend(results_for_this_level)
        return results
        