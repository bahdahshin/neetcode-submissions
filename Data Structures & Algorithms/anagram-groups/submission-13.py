class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict

        h = defaultdict(list)
        for kk, vv in enumerate(strs):
            c = Counter(vv)
            print(c.items())
            h[frozenset(c.items())].append(vv)

        a = []
        for kk, vv in h.items():
            a.append(vv)

        return a