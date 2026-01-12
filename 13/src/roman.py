class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
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
        for i in range(str_length):
            value = r_map[s[i]]
            if i == str_length - 1:
                total += value
            else:
                next_value = r_map[s[i+1]]
                if value < next_value:
                    total -= value
                else:
                    total += value
        return total
