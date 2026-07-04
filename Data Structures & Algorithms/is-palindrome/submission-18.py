class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c for c in s if c.isalnum()]
        b = "".join(a).lower()
        return b == b[::-1]