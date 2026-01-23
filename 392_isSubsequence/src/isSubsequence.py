class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i, char in enumerate(s):
            if char not in t:
                return False
            position = t.find(char)
            if position >= 0:
                t = t[position + 1:]
            else:
                return False
        return True
