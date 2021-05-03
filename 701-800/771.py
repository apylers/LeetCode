class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        S_dict = dict()
        for i in S:
            # 计算 S 中每个元素出现次数，存入字典
            S_dict[i] = S_dict.get(i, 0) + 1

        result = 0
        for i in J:
            # 计算为宝石的元素个数
            result += S_dict.get(i, 0)
        return result


J = "aA"
S = "aAAbbbb"
result = Solution().numJewelsInStones(J, S)
print(result)
