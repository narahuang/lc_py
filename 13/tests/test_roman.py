import pytest
from src.roman import Solution
sol = Solution()

@pytest.mark.parametrize("s, expected", [
    ('III', 3),
    ('IV', 4),
    ('IX', 9),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
    ('MCMXCIX', 1999),
    ('MMXXVI', 2026)
])
def test_romanToInt(s, expected):
    assert sol.romanToInt(s) == expected