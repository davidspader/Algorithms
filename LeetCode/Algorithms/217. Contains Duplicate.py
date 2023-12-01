class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums) - 1):
            for x in range(i + 1, len(nums)):
                if nums[i] == nums[x]:
                    return True
                
        return False

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False
    

'''
The second solution, which employs two nested for loops to compare all pairs of elements in the list, 
may be favored in specific scenarios due to its simplicity and lack of reliance on additional data structures. 
However, it has a quadratic time complexity (O(n^2)), making it less efficient for large lists. The first solution, 
using a set (hashset), provides a linear time complexity (O(n)), which is generally more efficient for sizable datasets, 
making it a preferred choice in terms of performance for duplicate detection in lists.
'''