class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for _, s in enumerate(strs):
            alphabetLst = [0] * 26
            for _, c in enumerate(s):
                alphabetLst[ord(c) - ord('a')] += 1
            group[tuple(alphabetLst)].append(s)
        return list(group.values())