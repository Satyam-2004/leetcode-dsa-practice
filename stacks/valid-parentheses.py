class Solution:
    def isValid(self, s: str) -> bool:
        hashy = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stk = []
        for c in s:
            if c not in hashy:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashy[c]:
                        return False
        return not stk