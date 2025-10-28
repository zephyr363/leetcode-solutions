from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        You are given an array of integers nums,
        there is a sliding window of size k which is moving from the very left of the array to the very right.
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.
        Return the max sliding window.
        """
        dq = deque() 
        res = []

        for i, num in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


s = Solution()
