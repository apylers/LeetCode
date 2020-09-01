from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        count = len(nums)
        dp = [[-1] * count for _ in range(count)]
        # dp[i][j] 表示剩余 nums[i : j + 1] 时当前玩家与另一玩家的最大分数差

        for i in range(count):
            # 仅一个数，当前玩家取走，另一玩家零分
            dp[i][i] = nums[i]

        for i in range(count - 2, -1, -1):
            for j in range(i + 1, count):
                # 最大差距：某一侧的数 - 剩余数在另一玩家处得到的最大差距
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][count - 1] >= 0


nums = [1, 5, 233, 7]
result = Solution().PredictTheWinner(nums)
print(result)
