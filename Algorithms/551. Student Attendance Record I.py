class Solution:
    def checkRecord(self, s: str) -> bool:
        absentC, consecutiveLateC = 0, 0

        for i in range(len(s)):
            if s[i] == 'A':
                absentC += 1
                consecutiveLateC = 0
            elif s[i] == 'L':
                consecutiveLateC += 1
            else:
                consecutiveLateC = 0
            
            if absentC > 1 or consecutiveLateC >= 3:
                return False
            
        return True