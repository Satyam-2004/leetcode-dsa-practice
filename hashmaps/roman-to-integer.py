class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        n = len(s)
        hashy = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        while i < n:
            if i < n - 1 and hashy[s[i]] < hashy[s[i + 1]]:
                total += hashy[s[i + 1]] - hashy[s[i]]
                i += 2
            else:
                total += hashy[s[i]]
                i += 1
        return total

