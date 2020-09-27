# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        current = root

        while current.val != p.val or current.val != q.val:
            if current.val > p.val and current.val > q.val:
                # 比 p q 都大，找左侧
                current = current.left
            elif current.val < p.val and current.val < q.val:
                # 比 p q 都小，找右侧
                current = current.right
            else:
                return current

        # 如果当前节点就是 p 或 q，则 q 或 p 必然为其子节点
        return current
