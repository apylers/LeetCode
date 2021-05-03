class Solution:
    def reverse(self, x: int) -> int:
        bound = (1 << 31) - 1
        result = 0
        sign = x >= 0
        x = abs(x)
        while x:
            temp = x % 10
            if bound / 10 - temp / 10 + (not sign) / 10 < result:
                return 0
            result = result * 10 + temp
            x //= 10
        if sign:
            return result
        return -result


x = -123
result = Solution().reverse(x)
print(result)
