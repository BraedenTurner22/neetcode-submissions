# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        dq = deque([(root, float('-inf'), float('inf'))])

        while dq:
            node, left, right = dq.popleft()

            if node.val <= left or node.val >= right:
                return False
            if node.left:
                dq.append((node.left, left, node.val))
            if node.right:
                dq.append((node.right, node.val, right))

        return True