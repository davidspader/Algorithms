from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            m = low + (high - low) // 2
            v = nums[m]

            if v == target:
                return m
            elif v > target:
                high = m
            else:
                low = m + 1
        return -1