from typing import List

class Solution:
    def singleNumber(nums: List[int]) -> int:
        for i in range(len(nums)):
            valueCount = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    valueCount += 1
            
            if valueCount == 1:
                return nums[i]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
    
'''
Algorithm 2 (XOR approach) is more efficient and clearer compared to Algorithm 1. 
It has a linear time complexity and is generally preferred for solving this type of problem.
'''