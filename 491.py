from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        # 以第一个元素初始化
        upper = {(nums[0],)}
        for num in nums[1:]:
            # 新加入元素添加进之前升序排列的部分中，再合并起来
            upper.update({seq + (num,) for seq in upper if seq[-1] <= num})
            # 最后添加该元素本身
            upper.add((num,))

        # 最后将单个元素剔除，并把元组转换成列表
        return [list(seq) for seq in upper if len(seq) > 1]


nums = [6, 4, 7, 6]
result = Solution().findSubsequences(nums)
print(result)
