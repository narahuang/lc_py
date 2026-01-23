class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        for i, char in enumerate(s):
            if char not in dict:
                if t[i] in dict.values():
                    return False
                dict[char] = t[i]
            else:
                if dict[char] != t[i]:
                    return False
        return True
