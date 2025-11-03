class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_str = str(x)

        return new_str == new_str[::-1]