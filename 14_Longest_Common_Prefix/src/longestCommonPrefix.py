

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        first_word = strs[0]
        result = ""
        match_list = []
        for i in range(len(first_word)):
            for word in strs[1:]:
                if i < len(word):
                    if first_word[i] == word[i]:
                        match_list.append(True)
                    else:
                        match_list.append(False)
                else:
                    match_list.append(False)
            if all(match_list):
                result += first_word[i]
            else:
                break
        return result
