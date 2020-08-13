class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 其中任一个为 0 就返回 0
        if num1 == "0" or num2 == "0":
            return "0"

        result = 0

        # num1 每一位与 num2 每一位相乘，再计算此结果需要左移多少位
        for i in range(-1, -len(num1) - 1, -1):
            for j in range(-1, -len(num2) - 1, -1):
                result += (
                    (ord(num1[i]) - ord("0"))
                    * (ord(num2[j]) - ord("0"))
                    * 10 ** (-i - j - 2)
                )

        # 转字符串
        result_str_back = ""
        while result > 0:
            current = result % 10
            result_str_back += chr(current + ord("0"))
            result //= 10
        return result_str_back[::-1]


num1 = "123"
num2 = "456"
result = Solution().multiply(num1, num2)
print(result)
print(type(result))
