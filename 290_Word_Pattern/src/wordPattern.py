class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i, char in enumerate(pattern):
            if char not in dict:
                if words[i] in dict.values():
                    return False
                dict[char] = words[i]
            else:
                if dict[char] != words[i]:
                    return False
        return True
