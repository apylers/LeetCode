# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            # 根节点不存在，返回 0
            return 0

        if not root.left:
            # 左节点不存在，返回右节点深度 + 1
            return self.minDepth(root.right) + 1
        left = self.minDepth(root.left)
        if not root.right:
            # 右节点不存在，返回左节点深度 + 1
            return left + 1
        right = self.minDepth(root.right)

        # 都存在，返回较小节点深度 + 1
        return min(left, right) + 1
