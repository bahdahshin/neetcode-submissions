class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}

        for _, v in enumerate(s):
            if v not in hashmapS:
                hashmapS[v] = 0
            else:
                hashmapS[v] = hashmapS[v] + 1

        for _, v in enumerate(t):
            if v not in hashmapT:
                hashmapT[v] = 0
            else:
                hashmapT[v] = hashmapT[v] + 1

        if hashmapS == hashmapT:
            return True
        else:
            return False