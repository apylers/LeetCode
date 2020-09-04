from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            # 根节点不存在，返回空数组
            return []

        # 获取左右子节点的结果
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        if not left + right:
            # 如果左右子节点皆空，返回自身值
            return ["{}".format(root.val)]

        # 否则将自身值加在最前方
        return ["{}->{}".format(root.val, child) for child in left + right]
