import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split()
        s = "".join(s)
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        text = cleaned_text.lower()
        if text == text[::-1]:
            return True
        else:
            return False
