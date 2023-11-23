class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)

        for c in countT:
            if countT[c] != countS.get(c,0):
                return False
            
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

'''
In a job interview, you might be asked to do the first implementation.

The first implementation uses a loop to count the occurrences of each 
character in both strings and compares the resulting dictionaries. 
Although functional, the dictionary approach adds complexity to the 
code compared to the second implementation that uses Counter. 

The third implementation, which uses the sorted function, is the simplest 
and most straightforward in terms of code, but it may be less efficient in terms of performance.
'''