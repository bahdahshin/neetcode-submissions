class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for k, v in enumerate(strs):
            c = Counter(v)
            d[frozenset(c.items())].append(v)

        l = []
        for i, (k, v) in enumerate(d.items()):
            l.append(v)

        return l