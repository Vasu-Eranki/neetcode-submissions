# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        hashmap = {}
        queue = [(0,root)]
        while (queue):
            length = len(queue)
            for _ in range(length):
                index, node = queue.pop(0)
                if index not in hashmap:
                    hashmap[index]=[node.val]
                else:
                    hashmap[index].append(node.val)
                if node.left:
                    queue.append((index-1,node.left))
                if node.right:
                    queue.append((index+1,node.right))
        hashmap_values = list(sorted(hashmap.items()))
        return [i[1] for i in hashmap_values]

        