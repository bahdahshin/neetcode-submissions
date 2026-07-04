class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [i for i in s if i.isalnum()]
        b = "".join(a).lower()
        return b == b[::-1]