"""
if two strings are match set of char, True
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for i, _ in enumerate(s):
            if s[i] not in hashS:
                hashS[s[i]] = 1
            else:
                hashS[s[i]] += 1

        for i, _ in enumerate(t):
            if t[i] not in hashT:
                hashT[t[i]] = 1
            else:
                hashT[t[i]] += 1

        if hashS == hashT:
            return True
        else:
            return False