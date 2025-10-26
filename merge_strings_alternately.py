from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        zipped = zip_longest(word1, word2, fillvalue='')
        return "".join(list(a + b for a,b in zipped))

s = Solution()

assert s.mergeAlternately("ab", "pqrs") == 'apbqrs'

