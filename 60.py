class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 获取需要用到的阶乘 0! ~ (n - 1)!
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)

        pre = k - 1  # 简单举例：第 1 个数实际上下标为 0
        nums = list(range(1, n + 1))

        string = ""
        for factorial in factorials[::-1]:
            # factorial 代表从左往右某一位确定之后右侧的总排列数
            index = pre // factorial  # nums[index] 即为要找的下一位
            string += str(nums.pop(index))  # 需要 pop，数不可重复
            pre = pre % factorial

        return string


n = 1
k = 1
result = Solution().getPermutation(n, k)
print(result)
