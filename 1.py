from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, i in enumerate(nums):
            if target - i in nums_dict:
                return [index, nums_dict[target - i]]
            nums_dict[i] = index
        return []


nums = [2, 5, 3, 7, 11, 15]
target = 10
result = Solution().twoSum(nums, target)
print(result)
