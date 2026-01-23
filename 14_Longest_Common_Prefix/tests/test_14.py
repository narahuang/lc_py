import pytest
from src.longestCommonPrefix import Solution
sol = Solution()


@pytest.mark.parametrize("s, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["ab", "a"], "a"),
    (["a"], "a"),
    (["cir", "car"], "c"),
    (["a", "a", "b"], "")
])
def test_romanToInt(s, expected):
    assert sol.longestCommonPrefix(s) == expected
