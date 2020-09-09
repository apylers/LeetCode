from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, target):
            """返回从 candidates[start] 开始满足加和为 target 的列表"""
            if target == 0:
                # target 为 0，不用任何 candidates
                return [[]]

            if start >= len(candidates):
                # 下标越界，返回空
                return []

            results = []
            for i in range(target // candidates[start] + 1):
                # candidates[start] 最多只能出现 target // candidates[start] 次
                remain = dfs(start + 1, target - i * candidates[start])  # 获取剩余数的列表
                result = [[candidates[start]] * i + item for item in remain]  # 添加前缀
                results += result  # 合并进 results
            return results

        return dfs(0, target)


candidates = [2, 3, 5, 7]
target = 8
result = Solution().combinationSum(candidates, target)
print(result)
