class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        lis1 = list(s)
        lis2 = lis1[::-1]
        if lis1 == lis2:
            return True
        else:
            return False