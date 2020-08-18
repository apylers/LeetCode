# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def generateBST(start, end):
            """由列表生成 BST"""
            if start > end:
                # 此时不存在节点
                return None

            # 取中心作为 BST 根节点
            mid = (start + end) // 2
            root = TreeNode(nodes[mid])

            # 寻找左右子节点
            root.left = generateBST(start, mid - 1)
            root.right = generateBST(mid + 1, end)

            return root

        # 链表转列表
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        root = generateBST(0, len(nodes) - 1)
        return root
