from typing import List
from functools import reduce


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            # 没有元素，返回空
            return []

        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def two_comb(comb, num):
            """
            comb: 前面数对应字符组成的列表
            num: 接下来的数字
            """
            return [i + j for i in comb for j in num_dict[num]]

        # reduce 完成递归操作，以 [""] 初始化
        return reduce(two_comb, digits, [""])


digits = "234"
result = Solution().letterCombinations(digits)
print(result)
