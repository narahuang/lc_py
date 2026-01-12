from src.roman import Solution
sol = Solution()

def test_3():
    assert sol.romanToInt('III') == 3
    
def test_4():
    assert sol.romanToInt('IV') == 4

def test_9():
    assert sol.romanToInt('IX') == 9

def test_58():
    assert sol.romanToInt('LVIII') == 58

def test_1994():
    assert sol.romanToInt('MCMXCIV') == 1994

def test_1999():
    assert sol.romanToInt('MCMXCIX') == 1999
    
def test_2026():
    assert sol.romanToInt('MMXXVI') == 2026