import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr):
            while airports[curr]:
                # 对子节点深度搜索
                next = heapq.heappop(airports[curr])
                dfs(next)
            # 子节点清空后当前节点变为最后一个节点，入栈
            stack.append(curr)

        # 保存机场对应关系并排序
        airports = collections.defaultdict(list)
        for depart, arrive in tickets:
            airports[depart].append(arrive)
        for key in airports:
            heapq.heapify(airports[key])

        stack = list()
        dfs("JFK")

        return stack[::-1]  # 逆向输出


tickets = [
    ["EZE", "TIA"],
    ["EZE", "HBA"],
    ["AXA", "TIA"],
    ["JFK", "AXA"],
    ["ANU", "JFK"],
    ["ADL", "ANU"],
    ["TIA", "AUA"],
    ["ANU", "AUA"],
    ["ADL", "EZE"],
    ["ADL", "EZE"],
    ["EZE", "ADL"],
    ["AXA", "EZE"],
    ["AUA", "AXA"],
    ["JFK", "AXA"],
    ["AXA", "AUA"],
    ["AUA", "ADL"],
    ["ANU", "EZE"],
    ["TIA", "ADL"],
    ["EZE", "ANU"],
    ["AUA", "ANU"],
]

result = Solution().findItinerary(tickets)
print(result)
