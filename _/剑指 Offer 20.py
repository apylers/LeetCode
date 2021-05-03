class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False


s = "0"
result = Solution().isNumber(s)
print(result)
