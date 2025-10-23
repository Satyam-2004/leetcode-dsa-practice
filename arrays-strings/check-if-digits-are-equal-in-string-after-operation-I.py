class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        while len(s) > 2:
            for i in range(len(s)-1):
                res = []
                num1 = int(s[i])
                num2 = int(s[i+1])
                mod = (num1 % num2) % 10
                res.append(str(mod))
            s = res

        return s[0] == s[1]
