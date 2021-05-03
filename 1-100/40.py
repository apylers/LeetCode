from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 修改 39 题做法
        def dfs(start, target):
            """返回从 candidates[start] 开始满足加和为 target 的列表"""
            if target == 0:
                # target 为 0，不用任何 candidates
                return [[]]

            if start >= len(candidates) or target < 0:
                # 下标越界或以超过目标值，返回空
                return []

            results = []
            for i in range(nums_count[candidates[start]] + 1):
                # candidates[start] 最多只能出现 nums_count[candidates[start]] 次
                remain = dfs(start + 1, target - i * candidates[start])  # 获取剩余数的列表
                result = [[candidates[start]] * i + item for item in remain]  # 添加前缀
                results += result  # 合并进 results
            return results

        nums_count = dict(Counter(candidates))  # 计算每个数出现次数
        candidates = list(set(candidates))  # 去重
        return dfs(0, target)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
result = Solution().combinationSum2(candidates, target)
print(result)
