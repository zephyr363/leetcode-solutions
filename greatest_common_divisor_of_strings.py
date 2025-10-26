import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_len = math.gcd(len(str1), len(str2))

        return str1[:gcd_len]

s = Solution()

assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
assert s.gcdOfStrings("LEET", "CODE") == ""

