class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_all_leaf(self, root: TreeNode):
        left, right = list(), list()
        if root.left:
            left = self.find_all_leaf(root.left)
        if root.right:
            right = self.find_all_leaf(root.right)
        if (not left) and (not right):
            return [root.val]
        return left + right

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1, leaf2 = self.find_all_leaf(root1), self.find_all_leaf(root2)
        return leaf1 == leaf2
