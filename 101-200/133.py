# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


# 深度优先
class Solution:
    def __init__(self):
        self.arrived = dict()  # 记录已经克隆的节点

    def cloneGraph(self, node: "Node") -> "Node":
        # 无任何节点，直接返回空
        if not node:
            return None

        # 节点出现过，返回克隆的节点
        if node in self.arrived:
            return self.arrived[node]

        clone_node = Node(node.val)  # 新建节点并赋值
        self.arrived[node] = clone_node  # 原节点与克隆节点对应储存

        clone_node.neighbors = [
            self.cloneGraph(neighbor) for neighbor in node.neighbors
        ]  # 深度优先，获得克隆后的邻接节点

        return clone_node
