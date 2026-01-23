import pytest
from src.strStr import Solution
sol = Solution()


@pytest.mark.parametrize("haystack, needle, expected", [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1)
])
def test_strStr(haystack, needle, expected):
    assert sol.strStr(haystack, needle) == expected
