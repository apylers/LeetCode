# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            """深度优先"""
            if not root:
                # 父节点为空，平衡，深度为 0
                return True, 0

            left_result, left_depth = dfs(root.left)  # 左子树平衡和深度
            right_result, right_depth = dfs(root.right)  # 右子树平衡和深度
            return (
                (
                    left_result and right_result and abs(left_depth - right_depth) < 2
                ),  # 左右均平衡且两者深度差小于 2
                max(left_depth, right_depth) + 1,  # 父节点深度
            )

        result, _ = dfs(root)  # 根节点开始
        return result
