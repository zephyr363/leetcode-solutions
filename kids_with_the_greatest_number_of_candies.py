from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result: List[bool] = []
        for candy in candies:
            buffer = candy + extraCandies
            exp = buffer >= max(candies)
            result.append(exp)
        return result
s = Solution()


assert s.kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True] 