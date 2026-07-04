class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict
        h = defaultdict(list)
        for i in strs:
            c = Counter(i)
            h[frozenset(c.items())].append(i)
        
        a = []
        for _, v in h.items():
            a.append(v)
        return a