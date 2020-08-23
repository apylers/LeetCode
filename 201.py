class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # n & n - 1 得到这两数的最大公共前缀
            n &= n - 1
        # 循环结束时 n 即为 [m, n] 的最大公共前缀
        return n


m = 1
n = 2147483647
result = Solution().rangeBitwiseAnd(m, n)
print(result)
