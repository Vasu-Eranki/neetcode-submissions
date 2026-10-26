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
        results = []
        bfs = [root]
        while(bfs):
            length = len(bfs)
            for _ in range(length):
                root_of_interest = bfs.pop(0)
                if (root_of_interest.left):
                    bfs.append(root_of_interest.left)
                if (root_of_interest.right):
                    bfs.append(root_of_interest.right)
            results.append(root_of_interest.val)
        return results

        