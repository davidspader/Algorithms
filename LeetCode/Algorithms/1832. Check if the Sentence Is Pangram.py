class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashset = set()

        for s in sentence:
            hashset.add(s)

        return len(hashset) == 26