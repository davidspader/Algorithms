from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        result = []
        first = [1]
        result.append(first)

        for i in range(1, numRows):
            prev = result[i - 1]
            current = [1]

            for j in range(1, i):
                current.append(prev[j - 1] + prev[j])

            current.append(1)
            result.append(current)

        return result