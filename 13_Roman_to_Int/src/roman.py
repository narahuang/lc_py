class Solution:
    def romanToInt(self, s: str) -> int:
        r_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        str_length = len(s)
        total = r_map[s[str_length - 1]]
        for i in range(str_length - 1):
            value = r_map[s[i]]
            next_value = r_map[s[i+1]]
            if value < next_value:
                total -= value
            else:
                total += value
        return total
