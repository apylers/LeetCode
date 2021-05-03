from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 储存所有数字出现次数
        count_dict = dict()
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        # 从大到小排列
        sort_count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

        # 返回数字
        return [item[0] for item in sort_count_dict][:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
result = Solution().topKFrequent(nums, k)
print(result)
