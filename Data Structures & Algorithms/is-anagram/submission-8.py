class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        ss = Counter(s)
        tt = Counter(t)
        if ss == tt:
            return True
        else:
            return False