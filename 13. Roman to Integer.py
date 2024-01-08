class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        n = 0
        for c in s:
            n += values[c]
            
        return n

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans
    

'''
The first solution uses string replacements to handle special patterns before calculating the value.
The second solution makes direct comparisons while iterating through the original string.

Both approaches are valid, but the choice between them may depend on personal preferences or specific requirements. 
The second solution, which performs direct comparisons, may be considered more readable and closer to the 
mathematical logic of converting Roman numerals to integers. The first solution, with string replacements, 
can be seen as a way to simplify the process before conversion.
'''