from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        result = list()

        i = 0

        while nums[i] <= 0 and i < len(nums) - 2:
            target = -nums[i]
            m = i + 1
            n = len(nums) - 1

            while m < n:
                if nums[m] + nums[n] < target:
                    m += 1
                elif nums[m] + nums[n] > target:
                    n -= 1
                else:
                    result.append([-target, nums[m], nums[n]])
                    m += 1
                    while nums[m] == nums[m - 1] and m < n:
                        m += 1
                    n -= 1
                    while nums[n] == nums[n + 1] and n > m:
                        n -= 1

            i += 1
            while nums[i] == nums[i - 1] and i < len(nums) - 2:
                i += 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
result = Solution().threeSum(nums)
print(result)
