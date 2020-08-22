from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len == 1:
            # 仅剩一个数，判断与 24 的大小关系，存在除法，考虑精度范围
            return abs(nums[0] - 24) < 0.000001

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                # nums 中挑出组合数 nums[i], nums[j]
                num1 = nums[i]
                num2 = nums[j]

                # 两数的全部可能操作方式
                all_pos = [
                    num1 + num2,
                    num1 * num2,
                    num1 - num2,
                    num2 - num1,
                ]
                # 为 0 不能作除数
                if num2 != 0:
                    all_pos.append(num1 / num2)
                if num1 != 0:
                    all_pos.append(num2 / num1)

                remain_nums = nums[:i] + nums[i + 1 : j] + nums[j + 1 :]  # 剩余未被挑出的数
                for pos in all_pos:
                    result = self.judgePoint24(
                        remain_nums + [pos]
                    )  # 深度优先，将剩余数与操作结果合并后传参
                    if result:
                        return True

        # 所有操作都不能得出 24，返回 False
        return False


nums = [3, 3, 8, 8]  # 8 / (3 - 8 / 3) = 24
result = Solution().judgePoint24(nums)
print(result)
