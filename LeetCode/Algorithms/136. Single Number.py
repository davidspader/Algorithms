from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            valueCount = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    valueCount += 1
            
            if valueCount == 1:
                return nums[i]